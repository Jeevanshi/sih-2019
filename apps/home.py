import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.Div([
        dcc.Link('Go to GVA Sector', href='/gva-sectors')
    ]),
    html.Div([
        dcc.Link('Go to GVA Time Series', href='/gva-time-series')
    ]),
    html.Div([
        dcc.Link('Go to Agg. National Accounts', href='/agg_national_accounts')
    ])
    
])
