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

#web layout
app.layout = html.Div(children=[
    html.H1(children='Global Waste Compostion',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'

            }

            ),
    html.Div('World Waste Management', style={'textAlign': 'center'}),
    html.Div('Waste Composition percent based on region', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#&FDBFF'}),
    html.H3('Interactive Bar Chart', style={'color': '#df1e56'}),
    html.Div("This bar graph represents the percent compostion of overall waste by region"),
    dcc.Graph(id='bar1'),
    html.Div('please select a region', style={'color': '#ef3e18', 'margin':'10px'}),
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
        
                
    )
    
    
])

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


#filteredDF = df[df['region_id'] == 'NAC']
#values = ['composition_food_organic_waste_percent', 'composition_metal_percent']
#finalDF = filteredDF.groupby(['country_name'])['composition_food_organic_waste_percent'].sum().reset_index()

#filteredDF = filteredDF.apply(lambda x: x.str.strip() if x.dtype == "NA" else x)

#df = px.data.gapminder().query("country_name == Aruba")

#df.loc[df["gdp"] < 10000, "country_name"]



#fig = px.bar(filteredDF, x='country_name', y='composition_food_organic_waste_percent')
#fig = px.pie(filteredDF, values=values, names='country_name', title="test pie graph")
#fig = px.pie(finalDF, values="composition_food_organic_waste_percent", names="country_name", title="test pie graph")

#fig.show()

#if __name__ == '__main__':
#    app.run_server()

app.run_server(debug=True)