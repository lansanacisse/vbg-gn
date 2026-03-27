"""
Page de connexion pour les associations partenaires.
"""

import dash
from dash import dcc, html, callback, Input, Output, State, no_update

dash.register_page(__name__, path="/connexion", title="Connexion – VBG Guinée", order=3)
import dash_bootstrap_components as dbc
from flask import session

from config import ADMIN_PASSWORD


def layout():
    return html.Div(
        [
            # ── Hero ──────────────────────────────────────────────────
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
            # ── Formulaire de connexion ────────────────────────────────
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
                                    html.Div(
                                        [
                                            html.H4(
                                                "Identification",
                                                className="section-title",
                                            ),
                                            html.P(
                                                "Renseignez le mot de passe de votre association.",
                                                className="section-subtitle",
                                            ),
                                        ]
                                    ),
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
                            html.Div(
                                id="login-feedback", style={"marginBottom": "12px"}
                            ),
                            dbc.Button(
                                "Se connecter",
                                id="login-btn",
                                n_clicks=0,
                                className="btn-primary-vbg",
                            ),
                        ],
                    ),
                ],
            ),
            # Redirection après connexion réussie
            dcc.Location(id="login-redirect", refresh=True),
        ]
    )


@callback(
    Output("login-feedback", "children"),
    Output("login-redirect", "pathname"),
    Input("login-btn", "n_clicks"),
    State("login-password", "value"),
    prevent_initial_call=True,
)
def handle_login(n_clicks, password):
    if not password:
        return dbc.Alert("Veuillez saisir le mot de passe.", color="danger"), no_update

    if password != ADMIN_PASSWORD:
        return dbc.Alert("Mot de passe incorrect.", color="danger"), no_update

    session["authenticated"] = True
    return no_update, "/espace/declarations"
