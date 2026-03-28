"""
Page de gestion des déclarations – espace associations.
Liste les cas pending avec actions valider / rejeter.
Accès restreint : redirige vers /connexion si non authentifié.
"""

import dash
from dash import html, callback, Input, Output, State, ctx, no_update, dcc
import dash_bootstrap_components as dbc
from flask import session

from database import get_session
from services.cases_service import get_pending_cases, update_case_status

dash.register_page(
    __name__,
    path="/espace/declarations",
    title="Déclarations – VBG Guinée",
    order=4,
)

STATUS_LABELS = {
    "pending":   ("En attente", "warning"),
    "validated": ("Validé",     "success"),
    "rejected":  ("Rejeté",     "danger"),
}


def layout():
    # Garde-fou côté layout : redirige si pas authentifié
    from flask import has_request_context
    if has_request_context() and not session.get("authenticated", False):
        return dcc.Location(href="/connexion", id="auth-guard", refresh=True)

    return html.Div([
        html.Div(
            style={"maxWidth": "1100px", "margin": "32px auto", "padding": "0 24px"},
            children=[
                html.H2(
                    "Déclarations en attente",
                    style={"color": "#4A235A", "fontWeight": 700, "marginBottom": "8px"},
                ),
                html.P(
                    "Examinez chaque déclaration et validez ou rejetez-la "
                    "pour qu'elle apparaisse dans les statistiques.",
                    style={"color": "#6B6B6B", "marginBottom": "28px"},
                ),
                html.Div(id="declarations-list"),
                dcc.Interval(id="declarations-refresh", interval=30_000, n_intervals=0),
            ],
        ),
    ])


def _case_card(case):
    status_label, status_color = STATUS_LABELS.get(case.status, ("Inconnu", "secondary"))
    age_str   = f"{case.victim_age} ans" if case.victim_age else "Non renseigné"
    genre_map = {"F": "Féminin", "M": "Masculin", "Autre": "Autre"}
    genre_str = genre_map.get(case.victim_gender, "Non renseigné")

    return html.Div(
        className="form-card",
        style={"marginBottom": "16px"},
        children=[
            dbc.Row([
                dbc.Col([
                    dbc.Badge(status_label, color=status_color, className="mb-2"),
                    html.H5(
                        f"{case.type_violence} — {case.region}, {case.prefecture}",
                        style={"fontWeight": 600, "color": "#2C2C2C", "margin": "4px 0"},
                    ),
                    html.P(
                        f"Date : {case.date_incident}  |  Âge : {age_str}  |  Genre : {genre_str}",
                        style={"fontSize": "0.88rem", "color": "#6B6B6B", "margin": 0},
                    ),
                    html.P(
                        f"Soumis le : {case.created_at.strftime('%d/%m/%Y à %H:%M') if case.created_at else 'N/A'}",
                        style={"fontSize": "0.82rem", "color": "#9B9B9B", "marginTop": "4px"},
                    ),
                ], md=8),
                dbc.Col([
                    dbc.Button(
                        "Valider",
                        id={"type": "btn-validate", "index": str(case.id)},
                        color="success", size="sm", className="w-100 mb-2",
                    ),
                    dbc.Button(
                        "Rejeter",
                        id={"type": "btn-reject", "index": str(case.id)},
                        color="danger", outline=True, size="sm", className="w-100",
                    ),
                ], md=4, style={"display": "flex", "flexDirection": "column", "justifyContent": "center"}),
            ], className="g-3"),
        ],
    )


@callback(
    Output("declarations-list", "children"),
    Input("declarations-refresh", "n_intervals"),
    Input({"type": "btn-validate", "index": dash.ALL}, "n_clicks"),
    Input({"type": "btn-reject",   "index": dash.ALL}, "n_clicks"),
    prevent_initial_call=False,
)
def update_declarations(n_intervals, validate_clicks, reject_clicks):
    triggered = ctx.triggered_id

    if isinstance(triggered, dict):
        case_id    = triggered["index"]
        new_status = "validated" if triggered["type"] == "btn-validate" else "rejected"
        db = get_session()
        try:
            update_case_status(db, case_id, new_status)
        finally:
            db.close()

    db = get_session()
    try:
        cases = get_pending_cases(db)
    finally:
        db.close()

    if not cases:
        return dbc.Alert(
            "Aucune déclaration en attente de validation.",
            color="success",
            style={"textAlign": "center"},
        )

    return [_case_card(c) for c in cases]