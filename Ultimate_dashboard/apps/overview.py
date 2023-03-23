import dash
import dash_echarts
import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback, dcc

import pandas as pd

df = pd.read_csv(r'C:\Users\Benjamin\pro_dashboard_dash\Final\data\test.csv')

option = {
    'xAxis': [{
        'type': 'category',
        'axisTick': {'show': True},
        'data': ['Jan', 'Fev', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    }],
    'yAxis': [{
        'type': 'value'
    }],
    'legend': {
        'data': list(map(str, df['legend'].tolist()))
    },
    'tooltip': {
        'trigger': 'axis',
        'axisPointer': {
            'type': 'shadow'
        }
    },
    'series': [
        {
            'name': '2020',
            'data': df[df['legend']==2020]['booking_days'].tolist(),
            'label': None,
            'barGap': 0,
            'emphasis': {
                'focus': 'series'
            },
            'type': 'bar',
        },
        {
            'name': '2021',
            'data': df[df['legend']==2021]['booking_days'].tolist(),
            'label': None,
            'barGap': 0,
            'emphasis': {
                'focus': 'series'
            },
            'type': 'bar',
        },
        {
            'name': '2022',
            'data': df[df['legend']==2022]['booking_days'].tolist(),
            'label': None,
            'barGap': 0,
            'emphasis': {
                'focus': 'series'
            },
            'type': 'bar',
        },
        {
            'name': '2023',
            'data': df[df['legend']==2023]['booking_days'].tolist(),
            'label': None,
            'barGap': 0,
            'emphasis': {
                'focus': 'series'
            },
            'type': 'bar',
        }
    ]
} 

overview_tab = html.Div([
    dmc.Card(
        children=[
            dash_echarts.DashECharts(
            option = option,
            id='echarts',
            style={
                "width": '100%',
                'height': '50vh'
            }
        )
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"width": '100%'},
    ),
    dcc.Interval(id="interval", interval=1 * 1000, n_intervals=0, max_intervals = 1),
])

@callback(
    Output('echarts', 'option'),
    [Input('interval', 'n_intervals')]
)
def update(n_intervals):
    return option