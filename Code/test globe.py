from flask.scaffold import F
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

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
    html.Div("This globe shows global population data"),
    dcc.Graph(id='globe1'),

    html.Div('Grey areas have not had information reported', style={'textAlign': 'center'}),

    html.Div('please select data to present', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='Data',
        value='population_population_number_of_people',
        options=[
            #we might need to recheck these later
            {'label': 'Total MSW', 'value': 'total_msw_total_msw_generated_tons_year'},
            {'label': 'GDP', 'value': 'gdp'},
            {'label': 'Percent of population covered by a waste system', 'value': 'waste_collection_coverage_total_percent_of_population'},
            {'label': 'Population', 'value': 'population_population_number_of_people'},

        ],
        
        
        ),
    
])
@app.callback(Output('globe1', 'figure'),
              [Input('Data', 'value')])

def displayGlobe(data):
    fig = px.scatter_geo(df, locations="iso3c",
                     color="region_id", # which column to use to set the color of markers
                     hover_name="country_name", # column added to hover information
                     size='population_population_number_of_people', # size of markers
                     projection="orthographic")
    #fig.update_geos(projection_type="orthographic")
    #fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})

    return fig            


app.run_server(debug=True)