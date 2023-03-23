import dash
import dash_echarts
import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback, dcc

import pandas as pd

df = pd.read_csv(r'C:\Users\Benjamin\LC-Clean\Ultimate_dashboard\data\occupancy_rate.csv')

option = {
    'xAxis': [{
        'type': 'category',
        'axisTick': {'show': True},
        #'data': ["Jan '20", "Fev '20", "Mar '20", "Apr '20", "May '20", "Jun '20", "Jul '20", "Aug '20", "Sep 20'", "Oct '20", "Nov '20", "Dec '20",
        #         "Jan '21", "Fev '21", "Mar '21", "Apr '21", "May '21", "Jun '21", "Jul '21", "Aug '21", "Sep 21'", "Oct '21", "Nov '21", "Dec '21",
        #         "Jan '22", "Fev '22", "Mar '22", "Apr '22", "May '22", "Jun '22", "Jul '22", "Aug '22", "Sep 22'", "Oct '22", "Nov '22", "Dec '22",
        #         "Jan '23", "Fev '23", "Mar '23", "Apr '23", "May '23", "Jun '23", "Jul '23", "Aug '23", "Sep 23'", "Oct '23", "Nov '23", "Dec '23"],
        'data' : list(map(str, df['period'].tolist())),
        'name': 'Sales Quantity',
    }],
    'yAxis': [{
        'type': 'value',
        'name': 'Sales Quantity',
    }],
    'legend': {
        'data': ['Occupancy Rate LC', 'Occupancy Rate ALL']
    },
    'tooltip': {
        'trigger': 'axis',
        'axisPointer': {
            'type': 'shadow'
        }
    },
    'series': [
        {
            'name': 'Occupancy Rate LC',
            'data': df['occupancy_rate_lc'].tolist(),
            'type': 'line',
            'symbol': None,
            'areaStyle': {
                    'color': 'rgba(58,77,233,0.1)'
            },
            'smooth': True,
        },
        {
            'name': 'Occupancy Rate ALL',
            'data': df['occupancy_rate_all'].tolist(),
            'type': 'line',
            'symbol': None,
            'areaStyle': {
                    'color': 'rgba(139,0,0,0.1)'
            },
            'smooth': True,
        },
    ]
} 

clients_tab = html.Div([
    dmc.Card(
        children=[
            dmc.CardSection(
                dmc.Group(
                    children=[
                        dmc.Text("Review Pictures", weight=500),
                        dmc.ChipGroup(
                            [dmc.Chip(x, value=x) for x in ["Weekly", "Monthly", "Yearly"]],
                            value="Weekly",
                        )
                    ],
                    position="apart",
                ),
                withBorder=True,
                inheritPadding=True,
                py="xs",
            ),
            dmc.CardSection(
                children=[
                    dash_echarts.DashECharts(
                    option = option,
                    id='echarts2',
                    style={
                        "width": '100%',
                        'height': '50vh'
                    }
               )
            ]
        )
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"width": '100%'},
    ),
    dcc.Interval(id="interval2", interval=1 * 1000, n_intervals=0, max_intervals = 1),
])

@callback(
    Output('echarts2', 'option'),
    [Input('interval2', 'n_intervals')]
)
def update(n_intervals):
    return option