import dash
from dash import dash_table, html, dcc

from dash.dependencies import Input, Output, State

import numpy as np
import pandas as pd
import plotly.graph_objs as go

import json


optionslist = ["Foo", "Bar", "Baz"]

################ APP ################


dropdown_cc = dcc.Dropdown(
       id='cc_drop',
       options=optionslist,
       multi=False,
       value='Foo'
   )

c = pd.read_csv('data/test.csv')

################ APP ################

app = dash.Dash(__name__)

server = app.server


app.layout = html.Div([


    html.Div([
        html.P("Hello, this is a test Dash app."),
        html.Div(' '.join(c['Country'])),
        html.Br(),
        dropdown_cc

    ],)
])




if __name__ == '__main__':
    app.run_server(debug=True)
