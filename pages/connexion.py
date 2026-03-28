"""
Page de connexion pour les associations partenaires.
"""

import dash
from dash import dcc, html, callback, Input, Output, State, no_update
import dash_bootstrap_components as dbc
from flask import session

from config import ADMIN_PASSWORD

dash.register_page(__name__, path="/connexion", title="Connexion – VBG Guinée", order=3)


def layout():
    # Si déjà connecté, renvoyer directement vers l'espace asso
    from flask import has_request_context
    if has_request_context() and session.get("authenticated", False):
        return dcc.Location(href="/espace/declarations", id="already-auth", refresh=True)

    return html.Div([
        html.Div(
            className="hero",
            children=[
                html.H1("Espace associations"),
                html.P(
                    "Connectez-vous pour accéder aux déclarations, "
                    "les valider et consulter les statistiques complètes.",
                ),
            ],
        ),
        html.Div(
            className="form-section",
            children=[
                html.Div(
                    className="form-card",
                    children=[
                        html.Div(
                            className="form-section-header",
                            children=[
                                html.Span("01", className="section-number"),
                                html.Div([
                                    html.H4("Identification", className="section-title"),
                                    html.P(
                                        "Renseignez le mot de passe de votre association.",
                                        className="section-subtitle",
                                    ),
                                ]),
                            ],
                        ),
                        html.Label("Mot de passe *", className="filter-label"),
                        dbc.Input(
                            id="login-password",
                            type="password",
                            placeholder="Mot de passe",
                            className="form-control",
                            style={"marginBottom": "20px"},
                        ),
                        html.Div(id="login-feedback", style={"marginBottom": "12px"}),
                        dbc.Button(
                            "Se connecter",
                            id="login-btn",
                            n_clicks=0,
                            className="btn-primary-vbg",
                        ),
                        # refresh=True est indispensable pour que la navbar
                        # relise la session Flask après connexion
                        dcc.Location(id="login-redirect", refresh=True),
                    ],
                ),
            ],
        ),
    ])


@callback(
    Output("login-feedback",  "children"),
    Output("login-redirect",  "href"),
    Input("login-btn",        "n_clicks"),
    State("login-password",   "value"),
    prevent_initial_call=True,
)
def handle_login(n_clicks, password):
    if not password:
        return dbc.Alert("Veuillez saisir le mot de passe.", color="danger"), no_update
    if password != ADMIN_PASSWORD:
        return dbc.Alert("Mot de passe incorrect.", color="danger"), no_update

    session["authenticated"] = True
    # href déclenche la navigation ; refresh=True sur Location recharge la page
    # ce qui force la réévaluation du callback navbar dans app.py
    return no_update, "/espace/declarations"