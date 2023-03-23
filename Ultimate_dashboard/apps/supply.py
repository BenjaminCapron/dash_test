import dash
import dash_echarts
import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback, dcc

import pandas as pd

df = pd.read_csv(r'C:\Users\Benjamin\pro_dashboard_dash\Final\data\test.csv')

def create_table(df):
    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col) for col in columns])]
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]
    return table

supply_tab = html.Div([
    dmc.Card(
        children=[
            dmc.Table(create_table(df),
                striped=True,
                highlightOnHover=True,
                withBorder=True,
                withColumnBorders=True,
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"width": '100%'},
    ),
])