import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from tabs import sidepanel, navbar, tab1, tab2


import pandas as pd


df = pd.read_csv("Clean_Data_with_names.csv")
app.layout = html.Div([navbar.Navbar(), sidepanel.layout])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])

def render_content(tab):
    if tab == 'tab-1':
        return tab1.layout
    elif tab == 'tab-2':
        return tab2.layout


if __name__ == '__main__':
    app.run_server(debug = True)