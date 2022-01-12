import charts
import justpy as jp
import pandas as pd

spline = charts.spline_chart
all_data = pd.read_csv('./data/average-hourly-earnings.csv')
all_data = all_data.set_index('industries')
col = 'Professional, scientific and technical services '
data = all_data.loc[col, :]



def app():
    page = jp.QuasarPage()
    title = jp.QDiv(a=page, text="Quebec Average Hourly Earnings", classes="text-h4 text-center")
    chart = jp.HighCharts(a=page, options=spline)
    chart.options.title.text = "industry: " + col
    x = list(data.index)
    y = list(data.values)
    chart.options.xAxis.categories = x
    chart.options.series[0].data = y
    chart.options.series[0].name = "hourly earnings"
    return page

jp.justpy(app)



