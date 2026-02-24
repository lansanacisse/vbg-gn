"""
VBG Guinée – Application principale Dash.
Lancement : python app.py
"""

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

from config import APP_TITLE, APP_SECRET_KEY, DEBUG, PORT
from api import api_bp
import pages.dashboard as dashboard
import pages.submit_case as submit_case
import pages.contact_victime as contact_victime

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
    ],
    suppress_callback_exceptions=True,
    title=APP_TITLE,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
server = app.server
server.secret_key = APP_SECRET_KEY
server.register_blueprint(api_bp)

PRIMARY = "#4A235A"
ACCENT  = "#8E44AD"

navbar = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand("🟣 VBG Guinée", href="/", style={"fontWeight": 700, "fontSize": "1.15rem"}),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("📊 Tableau de bord",  href="/",          active="exact")),
                dbc.NavItem(dbc.NavLink("📝 Signaler un cas",  href="/signaler")),
                dbc.NavItem(dbc.NavLink("🤝 Contacter une association", href="/contacter",
                                        style={"background": "rgba(255,255,255,0.15)",
                                               "borderRadius": "8px"})),
                dbc.NavItem(dbc.NavLink("🔌 API", href="/api/stats", target="_blank")),
            ], navbar=True, className="ms-auto"),
            id="navbar-collapse", navbar=True,
        ),
    ], fluid=True),
    color=PRIMARY,
    dark=True,
    sticky="top",
    style={"borderBottom": f"3px solid {ACCENT}"},
)

app.layout = html.Div(
    style={"fontFamily": "'Inter', sans-serif"},
    children=[
        dcc.Location(id="url", refresh=False),
        navbar,
        html.Div(id="page-content"),
        html.Footer(
            style={
                "background": PRIMARY, "color": "rgba(255,255,255,0.7)",
                "textAlign": "center", "padding": "22px 20px", "fontSize": "0.82rem",
            },
            children=[
                html.P("© 2024 VBG Guinée – Plateforme nationale de recensement des VBG",
                       style={"margin": 0}),
                html.P([
                    "Urgence : ", html.Strong("116", style={"color": "#F1948A"}),
                    "  |  API : ",
                    html.A("/api/cases", href="/api/cases", style={"color": "rgba(255,255,255,0.5)"}),
                    " | ",
                    html.A("/api/stats", href="/api/stats", style={"color": "rgba(255,255,255,0.5)"}),
                ], style={"margin": "6px 0 0"}),
            ],
        ),
    ],
)


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/signaler":
        return submit_case.layout()
    if pathname == "/contacter":
        return contact_victime.layout()
    return dashboard.layout()


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)