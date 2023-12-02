import dash
import plotly.express as px
from dash import html, dcc, callback_context,Input, Output, State, ALL
import dash_bootstrap_components as dbc

import json
import pandas as pd
import csv

from components import loja2, loja3
from app import app

# ========= Layout ========= #
layout = dbc.Container([

     dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("TAB CELL",  style={'color': 'yellow'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
             html.H5("By VW CONTABILIDADE", style={'color': 'white'})
        ])
    ])
], style={'padding-top': '50px', 'margin-bottom': '100px'}, className='text-center'),
html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), "\tLOJA 2"], href="/loja2", active=True, style={'text-align': 'left'})),
                    html.Br(),
                    dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), "\tLOJA 3"], href="/loja3", active=True, style={'text-align': 'left'})),
                    html.Br(),
                    
                ], vertical="lg", pills=True, fill=True)
            ])
        ]),
], style={'height': '100vh', 'padding': '0px', 'position':'sticky', 'top': 0, 'background-color': '#232423'})
