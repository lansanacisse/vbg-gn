"""
Page de soumission d'un nouveau cas VBG.
"""

from datetime import date
from dash import dcc, html, callback, Input, Output, State, no_update
import dash_bootstrap_components as dbc

from config import REGIONS, TYPES_VIOLENCE
from services.cases_service import create_case
from database import get_session


def layout():
    return html.Div([

        # ── Hero
        html.Div(className="hero", children=[
            html.H1("Signaler un cas"),
            html.P("Tous les cas soumis sont examin\u00e9s avant publication."),
        ]),

        # ── Formulaire
        html.Div(className="form-section", children=[
            html.Div(className="form-card", children=[

                dbc.Row([
                    dbc.Col([
                        html.Label("R\u00e9gion *", className="filter-label"),
                        dcc.Dropdown(id="f-region",
                                     options=[{"label": r, "value": r} for r in REGIONS],
                                     placeholder="S\u00e9lectionner une r\u00e9gion\u2026"),
                    ], md=6),
                    dbc.Col([
                        html.Label("Pr\u00e9fecture *", className="filter-label"),
                        dbc.Input(id="f-prefecture", placeholder="Ex : Coyah", type="text",
                                  className="form-control"),
                    ], md=6),
                ], className="g-3 mb-3"),

                html.Label("Type de violence *", className="filter-label"),
                dcc.Dropdown(id="f-type",
                             options=[{"label": t, "value": t} for t in TYPES_VIOLENCE],
                             placeholder="S\u00e9lectionner un type\u2026",
                             style={"marginBottom": "20px"}),

                dbc.Row([
                    dbc.Col([
                        html.Label("Date de l\u2019incident *", className="filter-label"),
                        dbc.Input(id="f-date", type="date", max=str(date.today()),
                                  className="form-control"),
                    ], md=4),
                    dbc.Col([
                        html.Label("Genre de la victime", className="filter-label"),
                        dcc.Dropdown(id="f-gender",
                                     options=[
                                         {"label": "F\u00e9minin", "value": "F"},
                                         {"label": "Masculin",  "value": "M"},
                                         {"label": "Autre",     "value": "Autre"},
                                     ],
                                     placeholder="Genre\u2026"),
                    ], md=4),
                    dbc.Col([
                        html.Label("\u00c2ge de la victime", className="filter-label"),
                        dbc.Input(id="f-age", type="number", min=0, max=120,
                                  placeholder="\u00c2ge (ann\u00e9es)", className="form-control"),
                    ], md=4),
                ], className="g-3 mb-4"),

                html.Div(id="form-feedback", style={"marginBottom": "12px"}),

                dbc.Button(
                    "Soumettre le cas",
                    id="btn-submit",
                    n_clicks=0,
                    className="btn-primary-vbg",
                ),
            ]),
        ]),
    ])


@callback(
    Output("form-feedback", "children"),
    Output("f-region",      "value"),
    Output("f-prefecture",  "value"),
    Output("f-type",        "value"),
    Output("f-date",        "value"),
    Output("f-gender",      "value"),
    Output("f-age",         "value"),
    Input("btn-submit",     "n_clicks"),
    State("f-region",       "value"),
    State("f-prefecture",   "value"),
    State("f-type",         "value"),
    State("f-date",         "value"),
    State("f-gender",       "value"),
    State("f-age",          "value"),
    prevent_initial_call=True,
)
def submit_case(n_clicks, region, prefecture, type_v, date_str, gender, age):
    errors = []
    if not region:
        errors.append("La r\u00e9gion est obligatoire.")
    if not prefecture or not prefecture.strip():
        errors.append("La pr\u00e9fecture est obligatoire.")
    if not type_v:
        errors.append("Le type de violence est obligatoire.")
    if not date_str:
        errors.append("La date de l\u2019incident est obligatoire.")

    if errors:
        return (
            dbc.Alert([html.Ul([html.Li(e) for e in errors])],
                      color="danger", className="alert alert-danger"),
            no_update, no_update, no_update, no_update, no_update, no_update,
        )

    try:
        db = get_session()
        try:
            create_case(db, {
                "region":       region,
                "prefecture":   prefecture.strip(),
                "type_violence": type_v,
                "date_incident": date.fromisoformat(date_str),
                "victim_gender": gender,
                "victim_age":   int(age) if age else None,
            })
        finally:
            db.close()
    except Exception as exc:
        return (
            dbc.Alert(f"Erreur : {exc}", color="danger", className="alert alert-danger"),
            no_update, no_update, no_update, no_update, no_update, no_update,
        )

    success = dbc.Alert(
        [html.Strong("\u2705 Cas soumis avec succ\u00e8s."),
         html.Span(" Il sera examin\u00e9 avant publication.")],
        color="success", className="alert alert-success",
    )
    return success, None, "", None, "", None, ""
