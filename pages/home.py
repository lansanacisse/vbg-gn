"""
Page d'accueil – VBG Guinée.
Présentation du contexte et chiffres clés sur les VBG en Guinée.

Images à placer dans le dossier assets/ :
  - assets/hero-guinee.jpg         : photo de contexte (bannière principale)
  - assets/action-victimes.jpg     : photo pour la carte victimes/témoins
  - assets/action-associations.jpg : photo pour la carte associations
"""

import dash
from dash import html
import dash_bootstrap_components as dbc

from config import NUMERO_VBG, NUMERO_POLICE

dash.register_page(__name__, path="/", title="Accueil – VBG Guinée", order=0)


def layout():
    return html.Div([

        # ── Hero avec image ────────────────────────────────────────
        html.Div(
            style={"position": "relative", "overflow": "hidden", "marginBottom": "0"},
            children=[
                html.Img(
                    src="/assets/hero-guinee.jpg",
                    style={
                        "width": "100%", "height": "360px",
                        "objectFit": "cover", "objectPosition": "center",
                        "display": "block", "filter": "brightness(0.45)",
                    },
                ),
                html.Div(
                    style={
                        "position": "absolute", "top": 0, "left": 0, "right": 0, "bottom": 0,
                        "display": "flex", "flexDirection": "column",
                        "alignItems": "center", "justifyContent": "center",
                        "padding": "32px", "textAlign": "center", "color": "white",
                    },
                    children=[
                        html.H1("VBG Guinée", style={"fontWeight": 700, "fontSize": "2.6rem", "margin": "0 0 12px"}),
                        html.P(
                            "Plateforme nationale de recensement des violences basées sur le genre "
                            "en République de Guinée.",
                            style={"fontSize": "1.05rem", "opacity": 0.9, "maxWidth": "620px", "margin": "0 auto 20px"},
                        ),
                        html.Blockquote(
                            "Collecter une donnée, c'est reconnaître qu'une victime existe. "
                            "Analyser ces données, c'est construire le chemin vers sa protection.",
                            style={
                                "fontStyle": "italic", "fontSize": "0.92rem", "opacity": 0.8,
                                "maxWidth": "540px", "margin": "0 auto",
                                "borderLeft": "3px solid rgba(255,255,255,0.45)",
                                "paddingLeft": "16px", "textAlign": "left",
                            },
                        ),
                    ],
                ),
            ],
        ),

        # ── Chiffres clés ──────────────────────────────────────────
        html.Div(
            style={"maxWidth": "1100px", "margin": "44px auto", "padding": "0 24px"},
            children=[
                html.H2("La situation en Guinée", style={"color": "#4A235A", "fontWeight": 700, "marginBottom": "8px"}),
                html.P(
                    "La Guinée figure parmi les pays où la condition des femmes est la plus précaire. "
                    "Ces chiffres sont issus de rapports de la société civile guinéenne et d'organisations internationales.",
                    style={"color": "#6B6B6B", "marginBottom": "28px", "maxWidth": "760px"},
                ),
                dbc.Row([
                    dbc.Col([html.Div(className="kpi-card", children=[
                        html.P("Victimes de violences conjugales", className="kpi-label"),
                        html.H2("85 %", className="kpi-value"),
                    ])], md=4, className="mb-3"),
                    dbc.Col([html.Div(className="kpi-card", children=[
                        html.P("Touchées par des VBG", className="kpi-label"),
                        html.H2("92 %", className="kpi-value"),
                    ])], md=4, className="mb-3"),
                    dbc.Col([html.Div(className="kpi-card", children=[
                        html.P("Victimes d'excision (MGF)", className="kpi-label"),
                        html.H2("97 %", className="kpi-value"),
                    ])], md=4, className="mb-3"),
                ], className="g-3"),
                dbc.Row([
                    dbc.Col([html.Div(className="kpi-card", children=[
                        html.P("Filles scolarisées vs garçons (secondaire)", className="kpi-label"),
                        html.H2("74 %", className="kpi-value"),
                    ])], md=4, className="mb-3"),
                    dbc.Col([html.Div(className="kpi-card", children=[
                        html.P("Femmes au parlement (2022)", className="kpi-label"),
                        html.H2("29,6 %", className="kpi-value"),
                    ])], md=4, className="mb-3"),
                    dbc.Col([html.Div(className="kpi-card", children=[
                        html.P("Victimes non signalées", className="kpi-label"),
                        html.H2("3 / 4", className="kpi-value"),
                    ])], md=4, className="mb-3"),
                ], className="g-3"),
                html.P(
                    "Sources : Rapport de la société civile guinéenne pour l'EPU – OHCHR, "
                    "ONU Annuaire statistique 2024, PNUD Rapport sur le développement humain 2023-2024.",
                    style={"fontSize": "0.78rem", "color": "#9B9B9B", "marginTop": "10px"},
                ),
            ],
        ),

        html.Hr(style={"maxWidth": "1100px", "margin": "0 auto", "borderColor": "#F0E8F6"}),

        # ── Deux actions avec images ───────────────────────────────
        html.Div(
            style={"maxWidth": "1100px", "margin": "44px auto 60px", "padding": "0 24px"},
            children=[
                html.H2("Agir ensemble", style={"color": "#4A235A", "fontWeight": 700, "marginBottom": "8px"}),
                html.P(
                    "Deux façons de contribuer à la lutte contre les VBG en Guinée.",
                    style={"color": "#6B6B6B", "marginBottom": "28px"},
                ),
                dbc.Row([
                    dbc.Col([
                        html.Div(
                            className="form-card",
                            style={"padding": "0", "overflow": "hidden", "height": "100%"},
                            children=[
                                html.Img(
                                    src="/assets/action-victimes.jpg",
                                    style={"width": "100%", "height": "180px", "objectFit": "cover", "display": "block"},
                                ),
                                html.Div(style={"padding": "24px"}, children=[
                                    html.H4("Vous êtes victime ou témoin", style={"color": "#4A235A", "fontWeight": 700, "marginBottom": "10px"}),
                                    html.P(
                                        "Déclarez un incident en toute confidentialité. "
                                        "Nous vous orienterons vers une prise en charge adaptée.",
                                        style={"color": "#6B6B6B", "marginBottom": "18px"},
                                    ),
                                    dbc.Button("Déclarer un incident", href="/contacter", className="btn-primary-vbg"),
                                ]),
                            ],
                        ),
                    ], md=6, className="mb-3"),
                    dbc.Col([
                        html.Div(
                            className="form-card",
                            style={"padding": "0", "overflow": "hidden", "height": "100%"},
                            children=[
                                html.Img(
                                    src="/assets/action-associations.jpg",
                                    style={"width": "100%", "height": "180px", "objectFit": "cover", "display": "block"},
                                ),
                                html.Div(style={"padding": "24px"}, children=[
                                    html.H4("Vous êtes une association", style={"color": "#4A235A", "fontWeight": 700, "marginBottom": "10px"}),
                                    html.P(
                                        "Connectez-vous à l'espace associations pour signaler des cas, "
                                        "valider des déclarations et consulter les données.",
                                        style={"color": "#6B6B6B", "marginBottom": "18px"},
                                    ),
                                    dbc.Button("Accéder à l'espace associations", href="/connexion", className="btn-primary-vbg"),
                                ]),
                            ],
                        ),
                    ], md=6, className="mb-3"),
                ], className="g-3"),

                html.Div(className="urgency-banner", style={"marginTop": "32px"}, children=[
                    html.Strong("En cas de danger immédiat :"),
                    html.Span("  appelez le "),
                    html.Strong(NUMERO_VBG,    style={"fontSize": "1.1rem", "color": "#C0392B"}),
                    html.Span(" (numéro national VBG) ou le "),
                    html.Strong(NUMERO_POLICE, style={"fontSize": "1.1rem", "color": "#C0392B"}),
                    html.Span(" (police / gendarmerie)."),
                ]),
            ],
        ),
    ])