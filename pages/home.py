"""
Page d'accueil – VBG Guinée.
Présentation du contexte et chiffres clés sur les VBG en Guinée.
"""

from dash import html
import dash_bootstrap_components as dbc

from config import NUMERO_VBG, NUMERO_POLICE


def layout():
    return html.Div(
        [
            # ── Hero ──────────────────────────────────────────────────
            html.Div(
                className="hero",
                children=[
                    html.H1("VBG Guinée"),
                    html.P(
                        "Plateforme nationale de recensement des violences basées sur le genre "
                        "en République de Guinée.",
                    ),
                    html.Blockquote(
                        "Collecter une donnée, c'est reconnaître qu'une victime existe. "
                        "Analyser ces données, c'est construire le chemin vers sa protection."
                    ),
                ],
            ),
            # ── Chiffres clés ──────────────────────────────────────────
            html.Div(
                style={
                    "maxWidth": "1100px",
                    "margin": "40px auto",
                    "padding": "0 24px",
                },
                children=[
                    html.H2(
                        "La situation en Guinée",
                        style={
                            "color": "#4A235A",
                            "fontWeight": 700,
                            "marginBottom": "8px",
                        },
                    ),
                    html.P(
                        "La Guinée figure parmi les pays où la condition des femmes est la plus précaire. "
                        "Ces chiffres, issus de rapports de la société civile guinéenne et d'organisations "
                        "internationales, illustrent l'ampleur du phénomène.",
                        style={
                            "color": "#6B6B6B",
                            "marginBottom": "32px",
                            "maxWidth": "760px",
                        },
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Div(
                                        className="kpi-card",
                                        children=[
                                            html.P(
                                                "Victimes de violences conjugales",
                                                className="kpi-label",
                                            ),
                                            html.H2("85 %", className="kpi-value"),
                                        ],
                                    ),
                                ],
                                md=4,
                                className="mb-3",
                            ),
                            dbc.Col(
                                [
                                    html.Div(
                                        className="kpi-card",
                                        children=[
                                            html.P(
                                                "Touchées par des VBG",
                                                className="kpi-label",
                                            ),
                                            html.H2("92 %", className="kpi-value"),
                                        ],
                                    ),
                                ],
                                md=4,
                                className="mb-3",
                            ),
                            dbc.Col(
                                [
                                    html.Div(
                                        className="kpi-card",
                                        children=[
                                            html.P(
                                                "Victimes d'excision (MGF)",
                                                className="kpi-label",
                                            ),
                                            html.H2("97 %", className="kpi-value"),
                                        ],
                                    ),
                                ],
                                md=4,
                                className="mb-3",
                            ),
                        ],
                        className="g-3 mb-4",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Div(
                                        className="kpi-card",
                                        children=[
                                            html.P(
                                                "Filles scolarisées vs garçons (secondaire)",
                                                className="kpi-label",
                                            ),
                                            html.H2("74 %", className="kpi-value"),
                                        ],
                                    ),
                                ],
                                md=4,
                                className="mb-3",
                            ),
                            dbc.Col(
                                [
                                    html.Div(
                                        className="kpi-card",
                                        children=[
                                            html.P(
                                                "Femmes au parlement (2022)",
                                                className="kpi-label",
                                            ),
                                            html.H2("29,6 %", className="kpi-value"),
                                        ],
                                    ),
                                ],
                                md=4,
                                className="mb-3",
                            ),
                            dbc.Col(
                                [
                                    html.Div(
                                        className="kpi-card",
                                        children=[
                                            html.P(
                                                "Victimes non signalées",
                                                className="kpi-label",
                                            ),
                                            html.H2("3 / 4", className="kpi-value"),
                                        ],
                                    ),
                                ],
                                md=4,
                                className="mb-3",
                            ),
                        ],
                        className="g-3",
                    ),
                    html.P(
                        "Sources : Rapport de la société civile guinéenne pour l'EPU – OHCHR, "
                        "ONU Annuaire statistique 2024, PNUD Rapport sur le développement humain 2023-2024.",
                        style={
                            "fontSize": "0.78rem",
                            "color": "#9B9B9B",
                            "marginTop": "12px",
                        },
                    ),
                ],
            ),
            # ── Séparateur ────────────────────────────────────────────
            html.Hr(
                style={
                    "maxWidth": "1100px",
                    "margin": "0 auto",
                    "borderColor": "#F0E8F6",
                }
            ),
            # ── Deux actions ───────────────────────────────────────────
            html.Div(
                style={
                    "maxWidth": "1100px",
                    "margin": "40px auto 60px",
                    "padding": "0 24px",
                },
                children=[
                    html.H2(
                        "Agir ensemble",
                        style={
                            "color": "#4A235A",
                            "fontWeight": 700,
                            "marginBottom": "8px",
                        },
                    ),
                    html.P(
                        "Deux façons de contribuer à la lutte contre les VBG en Guinée.",
                        style={"color": "#6B6B6B", "marginBottom": "32px"},
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Div(
                                        className="form-card",
                                        style={"height": "100%"},
                                        children=[
                                            html.H4(
                                                "Vous êtes victime ou témoin",
                                                style={
                                                    "color": "#4A235A",
                                                    "fontWeight": 700,
                                                    "marginBottom": "12px",
                                                },
                                            ),
                                            html.P(
                                                "Déclarez un incident en toute confidentialité. "
                                                "Nous vous orienterons vers une prise en charge adaptée.",
                                                style={
                                                    "color": "#6B6B6B",
                                                    "marginBottom": "20px",
                                                },
                                            ),
                                            dbc.Button(
                                                "Déclarer un incident",
                                                href="/contacter",
                                                className="btn-primary-vbg",
                                                external_link=False,
                                            ),
                                        ],
                                    ),
                                ],
                                md=6,
                                className="mb-3",
                            ),
                            dbc.Col(
                                [
                                    html.Div(
                                        className="form-card",
                                        style={"height": "100%"},
                                        children=[
                                            html.H4(
                                                "Vous êtes une association",
                                                style={
                                                    "color": "#4A235A",
                                                    "fontWeight": 700,
                                                    "marginBottom": "12px",
                                                },
                                            ),
                                            html.P(
                                                "Connectez-vous à l'espace associations pour signaler des cas, "
                                                "valider des déclarations et consulter les données.",
                                                style={
                                                    "color": "#6B6B6B",
                                                    "marginBottom": "20px",
                                                },
                                            ),
                                            dbc.Button(
                                                "Accéder à l'espace associations",
                                                href="/connexion",
                                                className="btn-primary-vbg",
                                                external_link=False,
                                            ),
                                        ],
                                    ),
                                ],
                                md=6,
                                className="mb-3",
                            ),
                        ],
                        className="g-3",
                    ),
                ],
            ),
        ]
    )
