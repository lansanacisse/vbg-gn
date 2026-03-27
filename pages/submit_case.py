"""
Page de soumission d'un nouveau cas VBG.
Destinée aux professionnels de terrain : associations, ONG, travailleurs sociaux.
"""

from datetime import date
from dash import dcc, html, callback, Input, Output, State, no_update
import dash_bootstrap_components as dbc

from config import (
    REGIONS,
    PREFECTURES,
    TYPES_VIOLENCE,
    NUMERO_VBG,
    NUMERO_POLICE,
)
from services.cases_service import create_case
from database import get_session


def layout():
    return html.Div(
        [
            # ── Hero bordeaux ──────────────────────────────────────────
            html.Div(
                className="hero-victime",
                children=[
                    html.H1("Espace professionnels"),
                    html.P(
                        "Enregistrez un cas observé sur le terrain. "
                        "Ces données alimentent les statistiques nationales après validation.",
                    ),
                ],
            ),
            # ── Bandeau info bordeaux ──────────────────────────────────
            html.Div(
                className="confidentiality-banner",
                children=[
                    html.Strong("Données à usage statistique uniquement."),
                    " Les informations saisies sont anonymisées et ne permettent pas "
                    "d'identifier la victime dans les publications.",
                ],
            ),
            # ── Formulaire ────────────────────────────────────────────
            html.Div(
                className="form-section",
                children=[
                    # ── Section 1 : Localisation ───────────────────────────
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
                                                "Localisation du cas",
                                                className="section-title",
                                            ),
                                            html.P(
                                                "Région et préfecture où l'incident s'est produit.",
                                                className="section-subtitle",
                                            ),
                                        ]
                                    ),
                                ],
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Région *", className="filter-label"
                                            ),
                                            dcc.Dropdown(
                                                id="f-region",
                                                options=[
                                                    {"label": r, "value": r}
                                                    for r in REGIONS
                                                ],
                                                placeholder="Sélectionner une région…",
                                            ),
                                        ],
                                        md=6,
                                    ),
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Préfecture *", className="filter-label"
                                            ),
                                            dcc.Dropdown(
                                                id="f-prefecture",
                                                options=[],
                                                placeholder="Sélectionner d'abord une région…",
                                                disabled=True,
                                            ),
                                        ],
                                        md=6,
                                    ),
                                ],
                                className="g-3",
                            ),
                        ],
                    ),
                    html.Div(style={"height": "20px"}),
                    # ── Section 2 : Nature du cas ──────────────────────────
                    html.Div(
                        className="form-card",
                        children=[
                            html.Div(
                                className="form-section-header",
                                children=[
                                    html.Span("02", className="section-number"),
                                    html.Div(
                                        [
                                            html.H4(
                                                "Nature du cas",
                                                className="section-title",
                                            ),
                                            html.P(
                                                "Type de violence et date de l'incident.",
                                                className="section-subtitle",
                                            ),
                                        ]
                                    ),
                                ],
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Type de violence *",
                                                className="filter-label",
                                            ),
                                            dcc.Dropdown(
                                                id="f-type",
                                                options=[
                                                    {"label": t, "value": t}
                                                    for t in TYPES_VIOLENCE
                                                ],
                                                placeholder="Sélectionner un type…",
                                            ),
                                        ],
                                        md=8,
                                    ),
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Date de l'incident *",
                                                className="filter-label",
                                            ),
                                            dbc.Input(
                                                id="f-date",
                                                type="date",
                                                max=str(date.today()),
                                                className="form-control",
                                            ),
                                        ],
                                        md=4,
                                    ),
                                ],
                                className="g-3",
                            ),
                        ],
                    ),
                    html.Div(style={"height": "20px"}),
                    # ── Section 3 : Profil de la victime ──────────────────
                    html.Div(
                        className="form-card",
                        children=[
                            html.Div(
                                className="form-section-header",
                                children=[
                                    html.Span("03", className="section-number"),
                                    html.Div(
                                        [
                                            html.H4(
                                                "Profil de la victime",
                                                className="section-title",
                                            ),
                                            html.P(
                                                "Informations démographiques anonymisées.",
                                                className="section-subtitle",
                                            ),
                                        ]
                                    ),
                                ],
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Genre de la victime",
                                                className="filter-label",
                                            ),
                                            dcc.Dropdown(
                                                id="f-gender",
                                                options=[
                                                    {"label": "Féminin", "value": "F"},
                                                    {"label": "Masculin", "value": "M"},
                                                    {
                                                        "label": "Autre",
                                                        "value": "Autre",
                                                    },
                                                ],
                                                placeholder="Genre…",
                                            ),
                                        ],
                                        md=6,
                                    ),
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Âge de la victime",
                                                className="filter-label",
                                            ),
                                            dbc.Input(
                                                id="f-age",
                                                type="number",
                                                min=0,
                                                max=120,
                                                placeholder="Âge en années",
                                                className="form-control",
                                            ),
                                        ],
                                        md=6,
                                    ),
                                ],
                                className="g-3",
                            ),
                        ],
                    ),
                    html.Div(style={"height": "20px"}),
                    # ── Envoi ──────────────────────────────────────────────
                    html.Div(
                        className="form-card",
                        children=[
                            html.Div(
                                id="form-feedback", style={"marginBottom": "12px"}
                            ),
                            dbc.Button(
                                "Soumettre le cas",
                                id="btn-submit",
                                n_clicks=0,
                                className="btn-primary-vbg",
                            ),
                            html.Div(
                                className="urgency-banner",
                                style={"marginTop": "24px"},
                                children=[
                                    html.Strong(
                                        "Si la victime est en danger immédiat :"
                                    ),
                                    html.Span("  orientez-la vers le "),
                                    html.Strong(
                                        NUMERO_VBG,
                                        style={
                                            "fontSize": "1.1rem",
                                            "color": "#C0392B",
                                        },
                                    ),
                                    html.Span(" (numéro national VBG) ou le "),
                                    html.Strong(
                                        NUMERO_POLICE,
                                        style={
                                            "fontSize": "1.1rem",
                                            "color": "#C0392B",
                                        },
                                    ),
                                    html.Span(" (police / gendarmerie)."),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ]
    )


# ── Callbacks ─────────────────────────────────────────────────────────────────


@callback(
    Output("f-prefecture", "options"),
    Output("f-prefecture", "disabled"),
    Input("f-region", "value"),
)
def update_prefectures(region):
    if not region:
        return [], True
    opts = [{"label": p, "value": p} for p in PREFECTURES.get(region, [])]
    return opts, False


@callback(
    Output("form-feedback", "children"),
    Output("f-region", "value"),
    Output("f-prefecture", "value"),
    Output("f-type", "value"),
    Output("f-date", "value"),
    Output("f-gender", "value"),
    Output("f-age", "value"),
    Input("btn-submit", "n_clicks"),
    State("f-region", "value"),
    State("f-prefecture", "value"),
    State("f-type", "value"),
    State("f-date", "value"),
    State("f-gender", "value"),
    State("f-age", "value"),
    prevent_initial_call=True,
)
def submit_case_callback(n_clicks, region, prefecture, type_v, date_str, gender, age):
    errors = []
    if not region:
        errors.append("La région est obligatoire.")
    if not prefecture:
        errors.append("La préfecture est obligatoire.")
    if not type_v:
        errors.append("Le type de violence est obligatoire.")
    if not date_str:
        errors.append("La date de l'incident est obligatoire.")

    if errors:
        return (
            dbc.Alert([html.Ul([html.Li(e) for e in errors])], color="danger"),
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
        )

    try:
        db = get_session()
        try:
            create_case(
                db,
                {
                    "region": region,
                    "prefecture": prefecture,
                    "type_violence": type_v,
                    "date_incident": date.fromisoformat(date_str),
                    "victim_gender": gender,
                    "victim_age": int(age) if age else None,
                },
            )
        finally:
            db.close()
    except Exception as exc:
        return (
            dbc.Alert(f"Erreur lors de l'enregistrement : {exc}", color="danger"),
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
            no_update,
        )

    success = dbc.Alert(
        [
            html.Strong("Cas soumis avec succès."),
            html.Span(" Il sera examiné par l'équipe avant publication."),
        ],
        color="success",
    )

    return success, None, None, None, None, None, None
