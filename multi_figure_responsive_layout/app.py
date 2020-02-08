import numpy as np

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import plotly_express as px

n_figures = 10


def make_figure():
    data = np.random.uniform(size=(32, 32))
    fig = (
        px.imshow(data, color_continuous_scale="Blues")
        .update_layout(
            coloraxis_showscale=False,
            margin=dict(l=0, r=0, b=0, t=0),  # noqa: E741
            height=210,
        )
        .update_xaxes(showticklabels=False)
        .update_yaxes(showticklabels=False)
    )
    return fig


def make_figure_section(n):
    col = dbc.Col(
        [
            html.Div(f"Figure {n}", id=f"fig_{n}_label", className="text-center mb-1"),
            dcc.Graph(
                id=f"fig_{n}_graph", figure=make_figure(), config={"staticPlot": True}
            ),
        ],
        lg=3,
        md=4,
        sm=6,
        className="mb-2 mt-1",
    )
    return col


body = dbc.Container(
    [
        html.Div(
            [
                html.H2("Multi-figure responsive layout"),
                html.P(
                    [
                        "This application demonstrates a responsive layout containing multiple "
                        "small figures wrapping over multiple rows depending of the window width."
                    ]
                ),
            ],
            className="mt-4",
        ),
        dbc.Row([make_figure_section(i) for i in range(n_figures)]),
        dbc.Row(
            dbc.Col(
                dbc.Button(
                    "Refresh Figures", id="refresh_button", color="primary", block=True,
                ),
                lg={"size": 4, "offset": 4},
                md={"size": 6, "offset": 3},
                width={"size": 8, "offset": 2},
            ),
            className="mt-3 mb-5",
        ),
    ]
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(body)

# Each figure can have its own callback as demonstrated here.
# Alternarively, a single, multi-output callback can be used to update all figures at once.
# The figure labels also have their individual ids and can be modified via callbacks.
for i in range(n_figures):

    @app.callback(
        Output(f"fig_{i}_graph", "figure"), [Input("refresh_button", "n_clicks")],
    )
    def refresh_figure(n_clicks):
        if n_clicks is not None:
            return make_figure()
        else:
            raise PreventUpdate


if __name__ == "__main__":
    app.run_server(debug=True)
