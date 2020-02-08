import numpy as np

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly_express as px


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
        dbc.Row([make_figure_section(i) for i in range(10)],),
    ]
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(body)

if __name__ == "__main__":
    app.run_server(debug=True)
