from pathlib import Path

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

assets_folder = Path().parent.joinpath("assets")

card1 = dbc.Card(
    [
        dbc.CardImg(src="/assets/code_4x6.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Coding", className="card-title"),
                html.P(
                    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis, unde "
                    "inventore? Ad sapiente consectetur quas sint?",
                    className="card-text",
                ),
            ],
        ),
        dbc.CardFooter(
            dbc.Button("Read More...", outline=True),
            className="bg-white border-top-0 pt-0",
        ),
    ],
    outline=True,
    className="h-100",
)

card2 = dbc.Card(
    [
        dbc.CardImg(src="/assets/aerial640.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Photography", className="card-title"),
                html.P(
                    "Lorem ipsum dolor sit amet consectetur adipisicing elit. "
                    "Aliquam, velit?",
                    className="card-text",
                ),
            ],
        ),
        dbc.CardFooter(
            dbc.Button("Read More...", outline=True),
            className="bg-white border-top-0 pt-0",
        ),
    ],
    # outline=True,
    className="h-100",
)

card3 = dbc.Card(
    [
        dbc.CardImg(src="/assets/appolo_4x6.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Space", className="card-title"),
                html.P(
                    "Lorem ipsum dolor sit, amet consectetur adipisicing elit.",
                    className="card-text",
                ),
            ],
        ),
        dbc.CardFooter(
            dbc.Button("Read More...", outline=True),
            className="bg-white border-top-0 pt-0",
        ),
    ],
    outline=True,
    className="h-100",
)

cards = dbc.Row(
    [
        dbc.Col(card1, md=6, lg=4, className="mb-4"),
        dbc.Col(card2, md=6, lg=4, className="mb-4"),
        dbc.Col(card3, md=6, lg=4, className="mb-4"),
    ]
)

body = dbc.Container(
    [
        html.H2("Cards Demo"),
        html.P("Wrapping Bootstrap cards of equal height with a button at the bottom."),
        dbc.Row(
            [
                dbc.Col(html.H3("Interests")),
                dbc.Col(dbc.Button("See All", outline=True, className="float-right")),
            ],
            className="mb-1",
        ),
        cards,
        html.P(
            [
                "Using ",
                html.Code('className="h-100"'),
                " ensures cards will use the full height of the parent row.",
            ]
        ),
    ],
    className="mt-4",
)

app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_folder=assets_folder,
)

app.layout = html.Div(body)

if __name__ == "__main__":
    app.run_server()
