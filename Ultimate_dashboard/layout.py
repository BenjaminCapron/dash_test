import dash
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_echarts
from dash import html, Output, Input, State, callback, dcc, html
import dash_auth

from apps.overview import overview_tab
from apps.supply import supply_tab
from apps.clients import clients_tab

app = dash.Dash(title="Data tool - Le Collectionist", update_title=None)
auth = dash_auth.BasicAuth(app, {'admin': 'admin'})
server = app.server 


header = dmc.Header(
            height=50,
            fixed=True,
            p="6px",
            children=[
                dmc.Container(
                    fluid=True,
                    style={"paddingRight": 12, "paddingLeft": 12},
                    children=dmc.Group(
                        position="apart",
                        align="flex-start",
                        children=[
                            dmc.Center(
                                dcc.Link(
                                    [
                                        dmc.MediaQuery(
                                            dmc.Group(
                                                spacing="4px",
                                                children=[
                                                    dmc.Image(
                                                        src="/assets/logo_vector.svg",
                                                        width=36,
                                                    ),
                                                    dmc.Text(
                                                        "Data tool",
                                                        size="lg",
                                                        color="gray",
                                                        weight=450,
                                                    ),
                                                ],
                                            ),
                                            smallerThan="xs",
                                            styles={"display": "none"},
                                        ),
                                        dmc.MediaQuery(
                                            dmc.Group(
                                                children=[
                                                    dmc.Image(
                                                        src="/assets/logo_vector.svg",
                                                        width=36,
                                                    ),
                                                ],
                                            ),
                                            largerThan="xs",
                                            styles={"display": "none"},
                                        ),
                                    ],
                                    href="/",
                                    style={"paddingTop": 3, "textDecoration": "none"},
                                ),
                            ),
                            dmc.Group(
                                position="right",
                                align="center",
                                spacing="xl",
                                children=[
                                    dmc.Select(
                                        id="app_choice",
                                        value="overview",
                                        data=[
                                            {"value": "overview", "label": "Overview"},
                                            {"value": "supply", "label": "Supply"},
                                            {"value": "clients", "label": "Clients"},
                                            {"value": "owners", "label": "Owners"},
                                            {"value": "chatgpt", "label": "ChatGPT"},
                                        ],
                                    ),
                                    html.A(
                                        dmc.ThemeIcon(
                                            DashIconify(
                                                icon="radix-icons:github-logo",
                                                width=22,
                                            ),
                                            radius=30,
                                            size=36,
                                            variant="outline",
                                            color="dark",
                                        ),
                                        href="https://github.com/",
                                        target="_blank",
                                    ),
                                    dmc.Button(
                                        "Filters",
                                        id="button-update",
                                        variant="outline",
                                        color="grape",
                                        leftIcon=[DashIconify(icon="radix-icons:update", width=20)],
                                    ),
                                    dmc.Modal(
                                        title="Filters",
                                        id="modal-update",
                                        centered=True,
                                        children=[
                                            dmc.Text("If you consider that datas are out of date, you may request an update.\n This request should be treated within 2 workings days."),
                                            dmc.Space(h=20),
                                            dmc.Group(
                                                [
                                                    dmc.Button("Submit", id="button-update-submit"),
                                                    dmc.Button(
                                                        "Close",
                                                        color="red",
                                                        variant="outline",
                                                        id="button-update-close",
                                                    ),
                                                ],
                                                position="right",
                                            ),
                                        ],
                                    )
                                ],
                            ),
                        ],
                    ),
                )
            ],
        )


CONTENT_STYLE = {
    "margin-left": "1px",
    "margin-right": "1px",
    "margin-top": "35px",
    "padding": "2rem 1rem",
    "background" :"#F5F7F8",
}

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([header, content])



@callback(
    Output("modal-update", "opened"),
    Input("button-update", "n_clicks"),
    Input("button-update-close", "n_clicks"),
    Input("button-update-submit", "n_clicks"),
    State("modal-update", "opened"),
    prevent_initial_call=True,
)
def modal_update_window(nc1, nc2, nc3, opened):
    return not opened

@callback(Output("page-content", "children"),
          Input("app_choice", "value"))
def select_value(value):
    if value=="overview":
        return overview_tab
    if value=="supply":
        return supply_tab
    if value=="clients":
        return clients_tab
    print(value)

app.run_server(debug=True)