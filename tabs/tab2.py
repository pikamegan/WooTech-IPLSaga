import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

from app import app 

df = pd.read_csv("Clean_Data_with_names.csv")

PAGE_SIZE = 50

fig = px.bar(df, x="Name", y="Player cost USD", color="Nationality(1=Overseas)", barmode="group")

layout = html.Div(children=[
    html.H1(children="Bar Chart of each IPL Player's Cost"),
    
    html.Div(children='''
        Simple bar chart showing player cost in USD for each player
    '''),
    
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

