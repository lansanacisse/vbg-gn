"""
VBG Guinée – Application principale Dash.
Lancement : python app.py
"""

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
from flask import session

from config import APP_TITLE, APP_SECRET_KEY, DEBUG, PORT, NUMERO_VBG
from api import api_bp
import pages.dashboard as dashboard
import pages.submit_case as submit_case
import pages.contact_victime as contact_victime
import pages.connexion as connexion
import pages.declarations as declarations
import pages.home as home

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

PROTECTED_PATHS = ["/espace/declarations", "/espace/signaler", "/espace/statistiques"]


def navbar_public():
    return dbc.Navbar(
        dbc.Container([
            dbc.NavbarBrand(APP_TITLE, href="/", style={"fontWeight": 700, "fontSize": "1.15rem"}),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Accueil",       href="/",               active="exact")),
                    dbc.NavItem(dbc.NavLink("Statistiques",   href="/statistiques")),
                    dbc.NavItem(dbc.NavLink("Déclarer un incident", href="/contacter")),
                    dbc.NavItem(dbc.NavLink(
                        "Espace associations",
                        href="/connexion",
                        style={"background": "rgba(255,255,255,0.15)", "borderRadius": "8px"},
                    )),
                ], navbar=True, className="ms-auto"),
                id="navbar-collapse", navbar=True,
            ),
        ], fluid=True),
        color=PRIMARY, dark=True, sticky="top",
        style={"borderBottom": f"3px solid {ACCENT}"},
    )


def navbar_authenticated():
    return dbc.Navbar(
        dbc.Container([
            dbc.NavbarBrand(APP_TITLE, href="/", style={"fontWeight": 700, "fontSize": "1.15rem"}),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Accueil",        href="/")),
                    dbc.NavItem(dbc.NavLink("Statistiques",   href="/statistiques")),
                    dbc.NavItem(dbc.NavLink("Déclarations",          href="/espace/declarations", active="exact")),
                    dbc.NavItem(dbc.NavLink("Signaler un cas",       href="/espace/signaler",     active="exact")),
                    dbc.NavItem(dbc.NavLink(
                        "Déconnexion",
                        href="/deconnexion",
                        style={"background": "rgba(255,255,255,0.15)", "borderRadius": "8px"},
                    )),
                ], navbar=True, className="ms-auto"),
                id="navbar-collapse", navbar=True,
            ),
        ], fluid=True),
        color=PRIMARY, dark=True, sticky="top",
        style={"borderBottom": f"3px solid {ACCENT}"},
    )


footer = html.Footer(
    style={
        "background": PRIMARY,
        "color": "rgba(255,255,255,0.7)",
        "textAlign": "center",
        "padding": "22px 20px",
        "fontSize": "0.82rem",
    },
    children=[
        html.P(
            f"© 2024 {APP_TITLE} – Plateforme nationale de recensement des VBG",
            style={"margin": 0},
        ),
        html.P([
            "Urgence : ",
            html.Strong(NUMERO_VBG, style={"color": "#F1948A"}),
            "  |  API : ",
            html.A("/api/cases", href="/api/cases", style={"color": "rgba(255,255,255,0.5)"}),
            " | ",
            html.A("/api/stats", href="/api/stats", style={"color": "rgba(255,255,255,0.5)"}),
        ], style={"margin": "6px 0 0"}),
    ],
)

app.layout = html.Div(
    style={"fontFamily": "'Inter', sans-serif"},
    children=[
        dcc.Location(id="url", refresh=False),
        html.Div(id="navbar-container"),
        html.Div(id="page-content"),
        footer,
    ],
)


@app.callback(
    Output("navbar-container", "children"),
    Output("page-content",     "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    authenticated = session.get("authenticated", False)

    # Déconnexion
    if pathname == "/deconnexion":
        session.clear()
        return navbar_public(), dcc.Location(href="/", id="logout-redirect", refresh=True)

    # Pages protégées — redirection si non connecté
    if pathname in PROTECTED_PATHS and not authenticated:
        return navbar_public(), dcc.Location(href="/connexion", id="auth-redirect", refresh=True)

    # Routing
    if pathname == "/connexion":
        if authenticated:
            return navbar_authenticated(), dcc.Location(href="/espace/declarations", id="already-auth", refresh=True)
        return navbar_public(), connexion.layout()

    if pathname == "/espace/declarations":
        return navbar_authenticated(), declarations.layout()

    if pathname == "/espace/signaler":
        return navbar_authenticated(), submit_case.layout()

    if pathname == "/contacter":
        return navbar_public(), contact_victime.layout()

    if pathname == "/statistiques":
        nav = navbar_authenticated() if authenticated else navbar_public()
        return nav, dashboard.layout()

    if pathname == "/espace/statistiques":
        return navbar_authenticated(), dashboard.layout()

    # Accueil par défaut
    nav = navbar_authenticated() if authenticated else navbar_public()
    return nav, home.layout()


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)