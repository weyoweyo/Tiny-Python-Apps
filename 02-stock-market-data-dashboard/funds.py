from bokeh.models.widgets import widget
from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from datetime import date

width = 800
height = 300


def get_data(name, data_source, start, end):
    df = data.DataReader(name, data_source, start, end)
    return df


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

output_file("fund.html")
show(p1)