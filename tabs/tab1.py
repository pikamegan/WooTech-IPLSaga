import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
import pandas as pd
from dash.dependencies import Input, Output

from app import app 

df = pd.read_csv("Clean_Data_with_names.csv")

PAGE_SIZE = 50


layout = html.Div([
    html.H6("Enter a player's name to find out how much they were sold at auction!"),
    html.Div(["Player name: ", dcc.Input(id='my-input', placeholder='Enter name here', type='text')]),
    html.Br(),
    html.Div(id='my-output'),
])
    
    
@app.callback(
    Output(component_id='my-output', component_property='children'), Input(component_id='my-input', component_property='value')
)

def update_output_div(input_value):
    if input_value in df['Name'].values:
        output_value = df.loc[df['Name'] == input_value, 'Player cost USD'].iloc[0]
        return 'Player cost in USD: $', output_value
    else:
        return 'Player not found'

