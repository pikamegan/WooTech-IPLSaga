import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
import pandas
from dash.dependencies import Input, Output

from app import app

from tabs import tab1, tab2

layout = html.Div([
    html.H1('IPL Data'),
    dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                    dcc.Tab(label='Player Cost', value='tab-1'),
                    dcc.Tab(label='Bar Graph', value='tab-2'),
                ])
            , html.Div(id='tabs-content')
        ]), width=9)])
  