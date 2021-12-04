from flask.scaffold import F
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import json

df = pd.read_csv("Datasets\Country level dataset.csv")

app = dash.Dash(__name__)



app.layout = html.Div(children=[
    html.H1(children='Global Waste Management',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'

            }

            ),
    #html.Div('World Waste Management', style={'textAlign': 'center'}),
    html.Div('Global waste information', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#&FDBFF'}),
    html.H3('Interactive Map', style={'color': '#df1e56'}),
    html.Div("This map represents different data for waste around the world"),
    dcc.Graph(id='map1'),

    html.Div('Grey areas have not had information reported', style={'textAlign': 'center'}),

    html.Div('please select data to present', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='Data',
        value='waste_collection_coverage_total_percent_of_population',
        options=[
            #we might need to recheck these later
            {'label': 'Total MSW', 'value': 'total_msw_total_msw_generated_tons_year'},
            {'label': 'GDP', 'value': 'gdp'},
            {'label': 'Percent of population covered by a waste system', 'value': 'waste_collection_coverage_total_percent_of_population'}
            

        ],
        
        
        ),
    
])


@app.callback(Output('map1', 'figure'),
              [Input('Data', 'value')])
def displayChoropleth(data):
    figure = go.Figure(data=go.Choropleth(
    locations = df['iso3c'],
    z = df[data],
    text = df['country_name'],
    colorscale = 'Blues',
    autocolorscale = True,
    reversescale = False,
    marker_line_color = 'darkgray',
    marker_line_width = 0.5,
    colorbar_tickprefix = '',
    colorbar_title = '',


    ) )

    return figure





app.run_server(debug=True)
