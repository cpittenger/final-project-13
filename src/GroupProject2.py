import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/CoronavirusTotal.csv')
df2 = pd.read_csv('../Datasets/CoronaTimeSeries.csv')
df3 = pd.read_csv('../Datasets/trafficData.csv')

app = dash.Dash()

# Bar Chart Data 2019
df4 = df3[['Location', 'FactValueNumeric']]
df4 = df4.iloc[:7]
data_barchart = [go.Bar(x=df4['Location'], y=df4['FactValueNumeric'])]

# Bar Chart Data 2018
df5 = df3[['Location', 'FactValueNumeric']]
df5 = df5.iloc[7:14]
data_barchart2 = [go.Bar(x=df5['Location'], y=df5['FactValueNumeric'])]

# Bar Chart Data 2017
df6 = df3[['Location', 'FactValueNumeric']]
df6 = df6.iloc[14:21]
data_barchart3 = [go.Bar(x=df6['Location'], y=df6['FactValueNumeric'])]

# Line Chart South-East Asia
dataLine = [[2012, 17.58],[2013, 17.13],[2014, 16.37],[2015, 16.00], [2016, 15.80], [2017, 15.75], [2018, 15.85], [2019, 15.84]]
line_df = pd.DataFrame(dataLine, columns = ['Year', 'Deaths'])
data_linechart1 = [go.Scatter(x=line_df['Year'], y=line_df['Deaths'], mode='lines', name='Death')]

# Line Chart Americas
dataLine = [[2012, 16.55],[2013, 16.07],[2014, 15.97],[2015, 15.78], [2016, 15.80], [2017, 15.72], [2018, 15.37], [2019, 15.33]]
line_df = pd.DataFrame(dataLine, columns = ['Year', 'Deaths'])
data_linechart2 = [go.Scatter(x=line_df['Year'], y=line_df['Deaths'], mode='lines', name='Death')]

# Line Chart Western Pacific
dataLine = [[2012, 18.52],[2013, 17.91],[2014, 16.37],[2015, 16.93], [2016, 16.80], [2017, 16.63], [2018, 16.51], [2019, 16.44]]
line_df = pd.DataFrame(dataLine, columns = ['Year', 'Deaths'])
data_linechart3 = [go.Scatter(x=line_df['Year'], y=line_df['Deaths'], mode='lines', name='Death')]

# Line Chart Eastern Mediterranean
dataLine = [[2012, 18.08],[2013, 17.74],[2014, 17.99],[2015, 17.96], [2016, 17.81], [2017, 17.56], [2018, 17.79], [2019, 17.82]]
line_df = pd.DataFrame(dataLine, columns = ['Year', 'Deaths'])
data_linechart4 = [go.Scatter(x=line_df['Year'], y=line_df['Deaths'], mode='lines', name='Death')]

# Line Chart Africa
dataLine = [[2012, 26.71],[2013, 26.43],[2014, 26.57],[2015, 26.67], [2016, 26.96], [2017, 26.88], [2018, 26.95], [2019, 27.21]]
line_df = pd.DataFrame(dataLine, columns = ['Year', 'Deaths'])
data_linechart5 = [go.Scatter(x=line_df['Year'], y=line_df['Deaths'], mode='lines', name='Death')]

# Line Chart Europe
dataLine = [[2012, 10.42],[2013, 9.98],[2014, 9.70],[2015, 9.18], [2016, 8.52], [2017, 8.08], [2018, 7.75], [2019, 7.40]]
line_df = pd.DataFrame(dataLine, columns = ['Year', 'Deaths'])
data_linechart6 = [go.Scatter(x=line_df['Year'], y=line_df['Deaths'], mode='lines', name='Death')]


# Multi Line Chart
multiline_df = df2
multiline_df['Date'] = pd.to_datetime(multiline_df['Date'])
trace1_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Death'], mode='lines', name='Death')
trace2_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Recovered'], mode='lines', name='Recovered')
trace3_multiline = go.Scatter(x=multiline_df['Date'], y=multiline_df['Unrecovered'], mode='lines', name='Under Treatment')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]


#trace1_multiline1 = go.Scatter(x=data_linechart1['Year'], y=data_linechart1['Deaths'], mode='lines', name='South-East Asia')
#trace1_multiline2 = go.Scatter(x=data_linechart2['Year'], y=data_linechart2['Deaths'], mode='lines', name='Americas')
#trace1_multiline3 = go.Scatter(x=data_linechart3['Year'], y=data_linechart3['Deaths'], mode='lines', name='Western Pacific')
#trace1_multiline4 = go.Scatter(x=data_linechart4['Year'], y=data_linechart4['Deaths'], mode='lines', name='Eastern Mediterranean')
#trace1_multiline5 = go.Scatter(x=data_linechart5['Year'], y=data_linechart5['Deaths'], mode='lines', name='Africa')
#trace1_multiline6 = go.Scatter(x=data_linechart6['Year'], y=data_linechart6['Deaths'], mode='lines', name='Europe')


#data_multiline2 = [trace1_multiline1, trace1_multiline2, trace1_multiline3, trace1_multiline4, trace1_multiline5, trace1_multiline6]
data_multiline2 = [data_linechart1, data_linechart2, data_linechart3, data_linechart4, data_linechart5, data_linechart6]


# Layout
app.layout = html.Div(children=[
    #Title
    html.H1(children='Web dashboard for Global Traffic Fatalities', style={'textAlign': 'center','color': '#046A38'}),
    html.Div('Group 13: Matthew Mango, Austin Black, Christian Amidon, Oliver Bond, Carl Pittenger', style={'textAlign': 'center'}),
    html.Div('', style={'textAlign': 'center'}),
    html.Br(),

    #2019 Bar chart
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    dcc.Graph(id='graph2', style={'color': '#B9975B'},
              figure={'data': data_barchart,'layout': go.Layout(title='Global Traffic Fatalities by Region, 2019',
                                      xaxis={'title': 'Region'}, yaxis={'title': 'Number of Deaths per 100,000'})}),

    #2018 Bar chart
    html.Br(),
    html.Hr(style={'color': '#046A38'}),
    dcc.Graph(id='graph3',
            figure={'data': data_barchart2,'layout': go.Layout(title='Global Traffic Fatalities by Region, 2018',
                                      xaxis={'title': 'Region'}, yaxis={'title': 'Number of Deaths per 100,000'})}),

    # 2017 Bar chart
    html.Br(),
    html.Hr(style={'color': '#046A38'}),
    dcc.Graph(id='graph4',
              figure={'data': data_barchart3,'layout': go.Layout(title='Global Traffic Fatalities by Region, 2017',
                                      xaxis={'title': 'Region'}, yaxis={'title': 'Number of Deaths per 100,000'})}),


    # ************************** Line Charts *********************
    # South-East Asia Line Chart
    html.Hr(style={'color': '#7FDBFF'}),
    dcc.Graph(id='graph5',
              figure={'data': data_linechart1,'layout': go.Layout(title='Annual Road Fatalies in South-East Asia',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Deaths per 100,000'})}),
    # Americas Line Chart
    html.Hr(style={'color': '#7FDBFF'}),
    dcc.Graph(id='graph6',figure={'data': data_linechart2,
                  'layout': go.Layout(title='Annual Road Fatalies in Americas',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Deaths per 100,000'})}),

    # Western Pacific Asia Line Chart
    html.Hr(style={'color': '#7FDBFF'}),
    dcc.Graph(id='graph7',
              figure={'data': data_linechart3,
                  'layout': go.Layout(title='Annual Road Fatalies in Western Pacific',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Deaths per 100,000'})}),

    # Eastern Mediterranean Line Chart
    html.Hr(style={'color': '#7FDBFF'}),
    dcc.Graph(id='graph8',
              figure={'data': data_linechart4,
                  'layout': go.Layout(title='Annual Road Fatalies in Eastern Mediterranean',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Deaths per 100,000'})}),

    # Africa Line Chart
    html.Hr(style={'color': '#7FDBFF'}),
    dcc.Graph(id='graph9',
              figure={'data': data_linechart5,
                  'layout': go.Layout(title='Annual Road Fatalies in Afria',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Deaths per 100,000'})}),

    # Europe Line Chart
    html.Hr(style={'color': '#7FDBFF'}),
    dcc.Graph(id='graph10',
              figure={'data': data_linechart6,
                  'layout': go.Layout(title='Annual Road Fatalies in Europe',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Deaths per 100,000'})}),


])


@app.callback(Output('graph1', 'figure'),
              [Input('select-continent', 'value')])
def update_figure(selected_continent):
    filtered_df = df1[df1['Continent'] == selected_continent]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    new_df = filtered_df.groupby(['Country'])['Confirmed'].sum().reset_index()
    new_df = new_df.sort_values(by=['Confirmed'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=new_df['Country'], y=new_df['Confirmed'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Corona Virus Confirmed Cases in '+selected_continent,
                                                                   xaxis={'title': 'Country'},
                                                                   yaxis={'title': 'Number of confirmed cases'})}

if __name__ == '__main__':
    app.run_server()
