"""
VBG Guinée – Application principale Dash.
Routing via Dash Pages (use_pages=True + register_page dans chaque page).
Lancement : python app.py
"""

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback
from flask import session

from config import APP_TITLE, APP_SECRET_KEY, DEBUG, PORT, NUMERO_VBG
from api import api_bp

PRIMARY = "#4A235A"
ACCENT  = "#8E44AD"

app = dash.Dash(
    __name__,
    use_pages=True,
    pages_folder="pages",
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


def navbar_public():
    return dbc.Navbar(
        dbc.Container([
            dbc.NavbarBrand(APP_TITLE, href="/", style={"fontWeight": 700, "fontSize": "1.15rem"}),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Accueil",              href="/")),
                    dbc.NavItem(dbc.NavLink("Statistiques",         href="/statistiques")),
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
                    dbc.NavItem(dbc.NavLink("Accueil",         href="/")),
                    dbc.NavItem(dbc.NavLink("Statistiques",    href="/statistiques")),
                    dbc.NavItem(dbc.NavLink("Déclarations",    href="/espace/declarations")),
                    dbc.NavItem(dbc.NavLink("Signaler un cas", href="/espace/signaler")),
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
        # refresh=True indispensable pour que Flask relise la session
        # après connexion/déconnexion
        dcc.Location(id="url", refresh=True),
        html.Div(id="navbar-container"),
        html.Div(id="deconnexion-trigger"),
        dash.page_container,
        footer,
    ],
)


@callback(
    Output("navbar-container",    "children"),
    Output("deconnexion-trigger", "children"),
    Input("url", "pathname"),
)
def update_navbar(pathname):
    """Bascule navbar + gère la déconnexion via l'URL /deconnexion."""
    # Déconnexion : vider la session et rediriger vers l'accueil
    if pathname == "/deconnexion":
        session.clear()
        return navbar_public(), dcc.Location(href="/", id="logout-redirect", refresh=True)

    authenticated = session.get("authenticated", False)
    navbar = navbar_authenticated() if authenticated else navbar_public()
    return navbar, ""


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)