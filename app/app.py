# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:09:17 2020

@author: reuben_sinha
"""
# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv("cash-surplus-deficit/data/cash-surp-def.csv")

df = df[df["Country Name"].isin(["Hong Kong SAR China","Hong Kong SAR China", "Afghanistan", "Bangladesh","Bhutan", "Maldives", "Myanmar", "Nepal", "India"])]

fig = px.line(df, x="Year", y="Value", color="Country Name")

app.layout = html.Div(children=[
    html.H1(children='GDP Trends in South Asia'),

    html.Div(children='''
        Dash: Sample Web application for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
