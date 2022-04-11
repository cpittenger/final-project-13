import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df3 = pd.read_csv("../data/trafficData.csv")

app = dash.Dash()

# Bar Chart Data 2019
df4 = df3[["Location", "FactValueNumeric"]]
df4 = df4.iloc[:7]
data_barchart = [go.Bar(x=df4["Location"], y=df4["FactValueNumeric"])]

# Bar Chart Data 2018
df5 = df3[["Location", "FactValueNumeric"]]
df5 = df5.iloc[7:14]
data_barchart2 = [go.Bar(x=df5["Location"], y=df5["FactValueNumeric"])]

# Bar Chart Data 2017
df6 = df3[["Location", "FactValueNumeric"]]
df6 = df6.iloc[14:21]
data_barchart3 = [go.Bar(x=df6["Location"], y=df6["FactValueNumeric"])]

# Line Chart South-East Asia
dataLine = [
    [2012, 17.58],
    [2013, 17.13],
    [2014, 16.37],
    [2015, 16.00],
    [2016, 15.80],
    [2017, 15.75],
    [2018, 15.85],
    [2019, 15.84],
]
line_df = pd.DataFrame(dataLine, columns=["Year", "Deaths"])
data_linechart1 = [
    go.Scatter(x=line_df["Year"], y=line_df["Deaths"], mode="lines", name="Death")
]

# Line Chart Americas
dataLine = [
    [2012, 16.55],
    [2013, 16.07],
    [2014, 15.97],
    [2015, 15.78],
    [2016, 15.80],
    [2017, 15.72],
    [2018, 15.37],
    [2019, 15.33],
]
line_df = pd.DataFrame(dataLine, columns=["Year", "Deaths"])
data_linechart2 = [
    go.Scatter(x=line_df["Year"], y=line_df["Deaths"], mode="lines", name="Death")
]

# Line Chart Western Pacific
dataLine = [
    [2012, 18.52],
    [2013, 17.91],
    [2014, 16.37],
    [2015, 16.93],
    [2016, 16.80],
    [2017, 16.63],
    [2018, 16.51],
    [2019, 16.44],
]
line_df = pd.DataFrame(dataLine, columns=["Year", "Deaths"])
data_linechart3 = [
    go.Scatter(x=line_df["Year"], y=line_df["Deaths"], mode="lines", name="Death")
]

# Line Chart Eastern Mediterranean
dataLine = [
    [2012, 18.08],
    [2013, 17.74],
    [2014, 17.99],
    [2015, 17.96],
    [2016, 17.81],
    [2017, 17.56],
    [2018, 17.79],
    [2019, 17.82],
]
line_df = pd.DataFrame(dataLine, columns=["Year", "Deaths"])
data_linechart4 = [
    go.Scatter(x=line_df["Year"], y=line_df["Deaths"], mode="lines", name="Death")
]

# Line Chart Africa
dataLine = [
    [2012, 26.71],
    [2013, 26.43],
    [2014, 26.57],
    [2015, 26.67],
    [2016, 26.96],
    [2017, 26.88],
    [2018, 26.95],
    [2019, 27.21],
]
line_df = pd.DataFrame(dataLine, columns=["Year", "Deaths"])
data_linechart5 = [
    go.Scatter(x=line_df["Year"], y=line_df["Deaths"], mode="lines", name="Death")
]

# Line Chart Europe
dataLine = [
    [2012, 10.42],
    [2013, 9.98],
    [2014, 9.70],
    [2015, 9.18],
    [2016, 8.52],
    [2017, 8.08],
    [2018, 7.75],
    [2019, 7.40],
]
line_df = pd.DataFrame(dataLine, columns=["Year", "Deaths"])
data_linechart6 = [
    go.Scatter(x=line_df["Year"], y=line_df["Deaths"], mode="lines", name="Death")
]

# Layout
app.layout = html.Div(
    children=[
        # Title
        html.H1(
            children="Web dashboard for Global Traffic Fatalities",
            style={"textAlign": "center", "color": "#046A38"},
        ),
        html.Div(
            "Group 13: Matthew Mango, Austin Black, Christian Amidon, Oliver Bond, Carl Pittenger",
            style={"textAlign": "center"},
        ),
        html.Div("", style={"textAlign": "center"}),
        html.Br(),
        # 2019 Bar chart
        html.Br(),
        html.Hr(style={"color": "#7FDBFF"}),
        dcc.Graph(
            id="graph2",
            style={"color": "#B9975B"},
            figure={
                "data": data_barchart,
                "layout": go.Layout(
                    title="Global Traffic Fatalities by Region, 2019",
                    xaxis={"title": "Region"},
                    yaxis={"title": "Number of Deaths per 100,000"},
                ),
            },
        ),
        # 2018 Bar chart
        html.Br(),
        html.Hr(style={"color": "#046A38"}),
        dcc.Graph(
            id="graph3",
            figure={
                "data": data_barchart2,
                "layout": go.Layout(
                    title="Global Traffic Fatalities by Region, 2018",
                    xaxis={"title": "Region"},
                    yaxis={"title": "Number of Deaths per 100,000"},
                ),
            },
        ),
        # 2017 Bar chart
        html.Br(),
        html.Hr(style={"color": "#046A38"}),
        dcc.Graph(
            id="graph4",
            figure={
                "data": data_barchart3,
                "layout": go.Layout(
                    title="Global Traffic Fatalities by Region, 2017",
                    xaxis={"title": "Region"},
                    yaxis={"title": "Number of Deaths per 100,000"},
                ),
            },
        ),
        # ************************** Line Charts *********************
        # South-East Asia Line Chart
        html.Hr(style={"color": "#7FDBFF"}),
        dcc.Graph(
            id="graph5",
            figure={
                "data": data_linechart1,
                "layout": go.Layout(
                    title="Annual Road Fatalies in South-East Asia",
                    xaxis={"title": "Year"},
                    yaxis={"title": "Deaths per 100,000"},
                ),
            },
        ),
        # Americas Line Chart
        html.Hr(style={"color": "#7FDBFF"}),
        dcc.Graph(
            id="graph6",
            figure={
                "data": data_linechart2,
                "layout": go.Layout(
                    title="Annual Road Fatalies in Americas",
                    xaxis={"title": "Year"},
                    yaxis={"title": "Deaths per 100,000"},
                ),
            },
        ),
        # Western Pacific Asia Line Chart
        html.Hr(style={"color": "#7FDBFF"}),
        dcc.Graph(
            id="graph7",
            figure={
                "data": data_linechart3,
                "layout": go.Layout(
                    title="Annual Road Fatalies in Western Pacific",
                    xaxis={"title": "Year"},
                    yaxis={"title": "Deaths per 100,000"},
                ),
            },
        ),
        # Eastern Mediterranean Line Chart
        html.Hr(style={"color": "#7FDBFF"}),
        dcc.Graph(
            id="graph8",
            figure={
                "data": data_linechart4,
                "layout": go.Layout(
                    title="Annual Road Fatalies in Eastern Mediterranean",
                    xaxis={"title": "Year"},
                    yaxis={"title": "Deaths per 100,000"},
                ),
            },
        ),
        # Africa Line Chart
        html.Hr(style={"color": "#7FDBFF"}),
        dcc.Graph(
            id="graph9",
            figure={
                "data": data_linechart5,
                "layout": go.Layout(
                    title="Annual Road Fatalies in Afria",
                    xaxis={"title": "Year"},
                    yaxis={"title": "Deaths per 100,000"},
                ),
            },
        ),
        # Europe Line Chart
        html.Hr(style={"color": "#7FDBFF"}),
        dcc.Graph(
            id="graph10",
            figure={
                "data": data_linechart6,
                "layout": go.Layout(
                    title="Annual Road Fatalies in Europe",
                    xaxis={"title": "Year"},
                    yaxis={"title": "Deaths per 100,000"},
                ),
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server()
