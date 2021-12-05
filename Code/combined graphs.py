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

#this will be the page we put all our graphs to have just one page

df = pd.read_csv("Datasets\Country level dataset.csv")
df2 = pd.read_csv("Datasets\City level dataset.csv")
df3 = pd.read_csv("Datasets\Country level dataset rounded.csv")
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
    html.H3('Interactive Map', style={'color': '#df1e56', 'textAlign': 'center'}),
    html.Div("This map represents different data for waste around the world", style={ 'textAlign': 'center'}),
    dcc.Graph(id='map1'),

    html.Div('Grey areas have not had information reported', style={'textAlign': 'center'}),

    html.Div('Please select data to present', style={'color': '#ef3e18', 'margin':'10px'}),
    html.Div('Current Data:'),
    dcc.Dropdown(
        id='Data',
        value='waste_collection_coverage_total_percent_of_population',
        options=[
            #we might need to recheck these later
            {'label': 'Total MSW (Measured in Tons)', 'value': 'total_msw_total_msw_generated_tons_year'},
            #{'label': 'GDP', 'value': 'gdp'},
            {'label': 'Percent of population covered by a waste system (PERCENTAGE)', 'value': 'waste_collection_coverage_total_percent_of_population'}
            

        ],
        
        
        ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#&FDBFF'}),
    html.H3('Interactive Bar Chart', style={'color': '#df1e56', 'textAlign': 'center'}),
    html.Div("This bar graph represents the percent compostion of overall waste by region", style={'textAlign': 'center'}),
    dcc.Graph(id='bar1'),
    html.Div('please select a region and composition type', style={'color': '#ef3e18', 'margin':'10px'}),
    html.Div('Current Data:'),
    dcc.Dropdown(
        id='select region',
        value='NAC',
        options=[
            #we might need to recheck these later
            {'label': 'North America', 'value': 'NAC'},
            {'label': 'South America', 'value': 'LCN'},
            {'label': 'Northern Asia', 'value': 'EAS'},
            {'label': 'Europe', 'value': 'ECS'},
            {'label': 'Southern Asia', 'value': 'SAS'},
            {'label': 'Africa', 'value': 'SSF'},
            {'label': 'Western/Central Asia', 'value': 'SSF'}

        ],
        
        
        ),
    
    dcc.Dropdown(
        id='Composition Type',
        value='composition_food_organic_waste_percent',
        options=[{'label': 'Food', 'value': 'composition_food_organic_waste_percent'},
                {'label': 'Glass', 'value': 'composition_glass_percent'},
                {'label': 'Metal', 'value': 'composition_metal_percent'},
                {'label': 'Other', 'value': 'composition_other_percent'},
                {'label': 'Paper/Cardboard', 'value': 'composition_paper_cardboard_percent'},
                {'label': 'Plastic', 'value': 'composition_plastic_percent'},
                {'label': 'Ruber/Leather', 'value': 'composition_rubber_leather_percent'},
                {'label': 'Wood', 'value': 'composition_wood_percent'},
                {'label': 'Green Waste', 'value': 'composition_yard_garden_green_waste_percent'}],
        
                
    ),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div("This bar graph represents the percent compostion of available city data by region", style={'textAlign': 'center'}),

    dcc.Graph(id='bar2'),
    html.Div('please select a region and composition type', style={'color': '#ef3e18', 'margin':'10px'}),
    html.Div('Empty bars have not had data reported', style={'textAlign': 'center'}),
    html.Div('Current Data:'),
    dcc.Dropdown(
        id='select region1',
        value='NAC',
        options=[
            #we might need to recheck these later
            {'label': 'North America', 'value': 'NAC'},
            {'label': 'South America', 'value': 'LCN'},
            {'label': 'Northern Asia', 'value': 'EAS'},
            {'label': 'Europe', 'value': 'ECS'},
            {'label': 'Southern Asia', 'value': 'SAS'},
            {'label': 'Africa', 'value': 'SSF'},
            {'label': 'Western/Central Asia', 'value': 'SSF'}

        ],
        
        
        ),
    
    dcc.Dropdown(
        id='Composition Type1',
        value='composition_food_organic_waste_percent',
        options=[{'label': 'Food', 'value': 'composition_food_organic_waste_percent'},
                {'label': 'Glass', 'value': 'composition_glass_percent'},
                {'label': 'Metal', 'value': 'composition_metal_percent'},
                {'label': 'Other', 'value': 'composition_other_percent'},
                {'label': 'Paper/Cardboard', 'value': 'composition_paper_cardboard_percent'},
                {'label': 'Plastic', 'value': 'composition_plastic_percent'},
                {'label': 'Ruber/Leather', 'value': 'composition_rubber_leather_percent'},
                {'label': 'Wood', 'value': 'composition_wood_percent'},
                {'label': 'Green Waste', 'value': 'composition_yard_garden_green_waste_percent'},
                #{'label': 'Total MSW', 'value': 'total_msw_total_msw_generated_tons_year'}
                ],
        
                
    ),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H3('Interactive Globe', style={'color': '#df1e56', 'textAlign': 'center'}),
    html.Div("This globe represents special types of waste in tons around the world, hover over for specific information", style={'textAlign': 'center'}),
    dcc.Graph(id='globe1'),
    html.Div('Areas with no bubbles or values of 0 have no data reported', style={'textAlign': 'center'}),

    html.Div('Please select data to present', style={'color': '#ef3e18', 'margin':'10px'}),
    html.Div('Current Data:'),
    dcc.Dropdown(
        id='Data for globe',
        value='special_waste_industrial_waste_tons_year',
        options=[
               
                {'label': 'Agricultural', 'value': 'special_waste_agricultural_waste_tons_year'},
                {'label': 'Construction Waste', 'value': 'special_waste_construction_and_demolition_waste_tons_year'},
                {'label': 'E waste', 'value': 'special_waste_e_waste_tons_year'},
                {'label': 'Hazardous', 'value': 'special_waste_hazardous_waste_tons_year'},
                {'label': 'Industrial', 'value': 'special_waste_industrial_waste_tons_year'},
                {'label': 'Medical', 'value': 'special_waste_medical_waste_tons_year'},
                #{'label': 'Total MSW', 'value': 'total_msw_total_msw_generated_tons_year'}
                ],
        
        
        ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
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

@app.callback(
            Output('bar1', 'figure'),
            [Input('select region', 'value'),
            Input('Composition Type', 'value')])
def updateFigure(selectedRegion, selectedComposition):
    filteredDF = df[df['region_id']==selectedRegion]
    filteredDF = filteredDF.apply(lambda x: x.str.strip() if x.dtype == "NA" else x)
    #finalDF = filteredDF.groupby([])
  
    fig = px.bar(filteredDF, x='country_name',y= selectedComposition, labels={selectedComposition: 'percentage', 'country_name': 'Country'} )
    return fig

@app.callback(
            Output('bar2', 'figure'),
            [Input('select region1', 'value'),
            Input('Composition Type1', 'value')])
def updateCityGraph(selectedRegion, selectedComposition):
    filteredDF = df2[df2['region_id']==selectedRegion]
    filteredDF = filteredDF.apply(lambda x: x.str.strip() if x.dtype == "NA" else x)
    #finalDF = filteredDF.groupby([])
  
    fig = px.bar(filteredDF, x='city_name',y= selectedComposition, labels={selectedComposition: 'percentage', 'city_name': 'City'} )
    return fig

@app.callback(
            Output('globe1', 'figure'),
            [Input('Data for globe', 'value'),
            ])
def updateGlobe(selectedData):
   
    figure= px.scatter_geo(df3, locations="iso3c",
                     color="region_id", # which column to use to set the color of markers
                     hover_name="country_name", # column added to hover information
                     
                     size= selectedData, # size of markers
                     projection="orthographic")
    return figure

app.run_server(debug=True)
