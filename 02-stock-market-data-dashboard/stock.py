from bokeh.models.annotations import ColorBar
from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from datetime import date
from bokeh.embed import components
from bokeh.resources import CDN 

width = 800
height = 300

def get_data(name, data_source, start, end):
    df = data.DataReader(name, data_source, start, end)
    return df

name="GOOG"
source="yahoo"
start=datetime.datetime(2021, 10, 1)
end=date.today()
df = get_data(name, source, start, end)
# High, Low, Open, Close, Volume, Adj Close
# print(df)

fig = figure(x_axis_type='datetime', plot_width=width, plot_height=height, sizing_mode="scale_width")
fig.title = "Candlestick chart: " + name


hours_12 = 12*60*60*1000 # half day in ms
increase = df.Close > df.Open
decrease = df.Close < df.Open
value = abs(df.Open-df.Close)
TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

fig.grid.grid_line_alpha=0.3
fig.segment(list(df.index), df.High, list(df.index), df.Low, color="black")
fig.vbar(df.index[increase], hours_12, df.Open[increase], df.Close[increase], fill_color="#D5E1DD", line_color="black")
fig.vbar(df.index[decrease], hours_12, df.Open[decrease], df.Close[decrease], fill_color="#F2583E", line_color="black")

# output_file("stock.html")
# show(fig)

script1, div1, = components(fig)
cdn_js = CDN.js_files[0]
