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

fig = go.Figure(data=go.Choropleth(
    locations = df['iso3c'],
    z = df['total_msw_total_msw_generated_tons_year'],
    text = df['country_name'],
    colorscale = 'Blues',
    autocolorscale = True,
    reversescale = False,
    marker_line_color = 'darkgray',
    marker_line_width = 0.5,
    colorbar_tickprefix = 'Tons ',
    colorbar_title = 'MSW Generated',


))



fig.show()