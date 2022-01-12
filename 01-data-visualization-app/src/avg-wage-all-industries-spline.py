import charts
import justpy as jp
import pandas as pd

area_spline = charts.areaspline_chart
all_data = pd.read_csv('./data/average-hourly-earnings.csv')
all_data = all_data.set_index('industries')
selected_industries = ['Goods producing industries ', 'Construction', 'Manufacturing  ', 'Trade  ', 
'Transportation and warehousing ', 'Finance and insurance  ', 'Real estate and rental and leasing  ', 
'Professional, scientific and technical services ', 'Health care and social assistance ', 'Accommodation and food services  ']
all_data = all_data.loc[selected_industries, :]

def app():
    page = jp.QuasarPage()
    title = jp.QDiv(a=page, text="Quebec Average Hourly Earnings", classes="text-h4 text-center")
    chart = jp.HighCharts(a=page, options=area_spline)
    chart.options.title.text = "all industries"
    chart.options.xAxis.categories = list(all_data.columns)
    chart.options.yAxis.title.text = "hourly earning"
    chart_data = [{"name": industry, "data": [v for v in all_data.loc[industry, :]]} 
                   for industry in list(all_data.index)]
    chart.options.series = chart_data
    return page

jp.justpy(app)


