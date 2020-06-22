from pathlib import Path

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

assets_folder = Path().parent.joinpath("assets")


def custom_card(id, title, text, image_src):
    card = html.Div(
        [
            html.Img(src=image_src, className="w-100"),
            html.H4(title, className="mt-3"),
            html.P(text),
            dbc.Button("Read More", color="primary", outline=True, className="mt-auto"),
        ],
        className="d-flex align-items-start flex-column h-100",
    )
    return card


card1 = dict(
    id="card1",
    title="Coding",
    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis, unde "
         "inventore? Ad sapiente consectetur quas sint?",
    image_src="assets/code_4x6.jpg"
)


card2 = dict(
    id="card2",
    title="Photography",
    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. "
         "Aliquam, velit?",
    image_src="assets/aerial640.jpg"
)


card3 = dict(
    id="card3",
    title="Space",
    text="Lorem ipsum dolor sit, amet consectetur adipisicing elit.",
    image_src="assets/appolo_4x6.jpg"
)


cards = dbc.Row(
    [
        dbc.Col(custom_card(**card1), md=6, lg=4, className="mb-4"),
        dbc.Col(custom_card(**card2), md=6, lg=4, className="mb-4"),
        dbc.Col(custom_card(**card3), md=6, lg=4, className="mb-4"),
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
    app.run_server(debug=True)
