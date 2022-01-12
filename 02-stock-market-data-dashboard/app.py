from flask import Flask, render_template
from bokeh.models.annotations import ColorBar
from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from datetime import date
from bokeh.embed import components
from bokeh.resources import CDN 


width = 800
height = 300
hours_12 = 12*60*60*1000 # half day in ms
name="GOOG"
source="yahoo"
start=datetime.datetime(2021, 10, 1)
end=date.today()

app=Flask(__name__)


def get_data(name, data_source, start, end):
    df = data.DataReader(name, data_source, start, end)
    return df

@app.route('/plot1/')
def plot1():
    df = get_data(name, source, start, end)
    fig = figure(x_axis_type='datetime', plot_width=width, plot_height=height, sizing_mode="scale_width")
    fig.title = "Candlestick chart: " + name   
    increase = df.Close > df.Open
    decrease = df.Close < df.Open
    value = abs(df.Open-df.Close)
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
    fig.grid.grid_line_alpha=0.3
    fig.segment(list(df.index), df.High, list(df.index), df.Low, color="black")
    fig.vbar(df.index[increase], hours_12, df.Open[increase], df.Close[increase], fill_color="#D5E1DD", line_color="black")
    fig.vbar(df.index[decrease], hours_12, df.Open[decrease], df.Close[decrease], fill_color="#F2583E", line_color="black")
    script1, div1, = components(fig)
    cdn_js = CDN.js_files[0]
    return render_template("plot.html", 
    script1=script1, 
    div1=div1, 
    cdn_js=cdn_js)


@app.route('/plot2/')
def plot2():
    start=datetime.datetime(2020, 1, 1)
    end=date.today()
    cibc_nasdaq = get_data("0P0000UQY8.TO", "yahoo", start, end)
    rbc_us_index = get_data("0P000070AD.TO", "yahoo", start, end)
    td_nasdaq = get_data("0P000071W5.TO", "yahoo", start, end)
    p1 = figure(x_axis_type="datetime", title="Mutual Fund Prices", plot_width=width, plot_height=height, sizing_mode="scale_width")
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'
    p1.line(list(cibc_nasdaq.index), cibc_nasdaq['Adj Close'], color='#FB9A99', legend_label='CIBC NASDAQ INDEX FUND')
    p1.line(list(cibc_nasdaq.index), rbc_us_index['Adj Close'], color='#B2DF8A', legend_label='RBC US INDEX FUND')
    p1.line(list(cibc_nasdaq.index), td_nasdaq['Adj Close'], color='#33A02C', legend_label='TD NASDAQ Index - e')
    p1.legend.location = "top_left"
    script2, div2, = components(p1)
    cdn_js2 = CDN.js_files[0]
    return render_template("plot2.html", 
    script2=script2, 
    div2=div2, 
    cdn_js2=cdn_js2)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)