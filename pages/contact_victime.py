"""
Page "Déclarer un incident" – Formulaire de prise en charge pour victimes/témoins VBG.
"""

from datetime import date
from dash import dcc, html, callback, Input, Output, State, no_update
import dash_bootstrap_components as dbc

from config import (
    REGIONS,
    PREFECTURES,
    TYPES_VIOLENCE,
    RELATIONS_AUTEUR,
    LIEUX_INCIDENT,
    BESOINS,
    NUMERO_VBG,
    NUMERO_POLICE,
)


def layout():
    return html.Div(
        [
            # ── Hero violet ────────────────────────────────────────────
            html.Div(
                className="hero-victime",
                children=[
                    html.H1("Vous n'êtes pas seul"),
                    html.P(
                        "Si vous êtes victime ou témoin de violences, vous pouvez nous le signaler "
                        "en toute confidentialité. Nous vous orienterons vers une prise en charge adaptée.",
                    ),
                ],
            ),
            # ── Bandeau confidentialité bleu ───────────────────────────
            html.Div(
                className="confidentiality-banner",
                children=[
                    html.Strong("Vos informations sont strictement confidentielles."),
                    " Votre déclaration nous aidera à mieux comprendre l'ampleur du problème "
                    "et à fournir un soutien approprié aux victimes.",
                ],
            ),
            # ── Formulaire ────────────────────────────────────────────
            html.Div(
                className="form-section",
                children=[
                    # ── Section 1 : Identité ───────────────────────────────
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
                                                "Informations personnelles",
                                                className="section-title",
                                            ),
                                            html.P(
                                                "Renseignez vos informations de base. Ces données sont confidentielles.",
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
                                                "Vous déclarez en tant que *",
                                                className="filter-label",
                                            ),
                                            dcc.Dropdown(
                                                id="cv-declarant",
                                                options=[
                                                    {
                                                        "label": "Victime directe",
                                                        "value": "victime",
                                                    },
                                                    {
                                                        "label": "Témoin",
                                                        "value": "temoin",
                                                    },
                                                    {
                                                        "label": "Membre de la famille",
                                                        "value": "famille",
                                                    },
                                                    {
                                                        "label": "Professionnel de santé / Social",
                                                        "value": "professionnel",
                                                    },
                                                ],
                                                placeholder="Sélectionner…",
                                            ),
                                        ],
                                        md=6,
                                    ),
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Souhaitez-vous rester anonyme ?",
                                                className="filter-label",
                                            ),
                                            dcc.Dropdown(
                                                id="cv-anonyme",
                                                options=[
                                                    {
                                                        "label": "Oui, je préfère rester anonyme",
                                                        "value": "oui",
                                                    },
                                                    {
                                                        "label": "Non, je consens à être contacté(e)",
                                                        "value": "non",
                                                    },
                                                ],
                                                placeholder="Choisir…",
                                                value="oui",
                                            ),
                                        ],
                                        md=6,
                                    ),
                                ],
                                className="g-3 mb-3",
                            ),
                            html.Div(id="cv-identity-fields"),
                        ],
                    ),
                    html.Div(style={"height": "20px"}),
                    # ── Section 2 : Localisation ───────────────────────────
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
                                                "Localisation de l'incident",
                                                className="section-title",
                                            ),
                                            html.P(
                                                "Où l'incident s'est-il produit ?",
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
                                                id="cv-region",
                                                options=[
                                                    {"label": r, "value": r}
                                                    for r in REGIONS
                                                ],
                                                placeholder="Sélectionner une région…",
                                            ),
                                        ],
                                        md=4,
                                    ),
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Préfecture *", className="filter-label"
                                            ),
                                            dcc.Dropdown(
                                                id="cv-prefecture",
                                                options=[],
                                                placeholder="Sélectionner d'abord une région…",
                                                disabled=True,
                                            ),
                                        ],
                                        md=4,
                                    ),
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Quartier / Village",
                                                className="filter-label",
                                            ),
                                            dbc.Input(
                                                id="cv-quartier",
                                                placeholder="Ex : Ratoma centre",
                                                className="form-control",
                                            ),
                                        ],
                                        md=4,
                                    ),
                                ],
                                className="g-3 mb-3",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Lieu de l'incident *",
                                                className="filter-label",
                                            ),
                                            dcc.Dropdown(
                                                id="cv-lieu",
                                                options=[
                                                    {"label": l, "value": l}
                                                    for l in LIEUX_INCIDENT
                                                ],
                                                placeholder="Où cela s'est-il passé ?",
                                            ),
                                        ],
                                        md=6,
                                    ),
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Date approximative de l'incident *",
                                                className="filter-label",
                                            ),
                                            dbc.Input(
                                                id="cv-date",
                                                type="date",
                                                max=str(date.today()),
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
                    # ── Section 3 : Contexte ───────────────────────────────
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
                                                "Contexte de la violence",
                                                className="section-title",
                                            ),
                                            html.P(
                                                "Ces informations nous permettent de mieux orienter l'aide.",
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
                                                id="cv-type-violence",
                                                options=[
                                                    {"label": t, "value": t}
                                                    for t in TYPES_VIOLENCE
                                                ],
                                                placeholder="Sélectionner un type…",
                                            ),
                                        ],
                                        md=6,
                                    ),
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Relation avec l'auteur présumé",
                                                className="filter-label",
                                            ),
                                            dcc.Dropdown(
                                                id="cv-relation",
                                                options=[
                                                    {"label": r, "value": r}
                                                    for r in RELATIONS_AUTEUR
                                                ],
                                                placeholder="Relation…",
                                            ),
                                        ],
                                        md=6,
                                    ),
                                ],
                                className="g-3 mb-3",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Âge de la victime",
                                                className="filter-label",
                                            ),
                                            dbc.Input(
                                                id="cv-age",
                                                type="number",
                                                min=0,
                                                max=120,
                                                placeholder="Âge en années",
                                                className="form-control",
                                            ),
                                        ],
                                        md=4,
                                    ),
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "Genre de la victime",
                                                className="filter-label",
                                            ),
                                            dcc.Dropdown(
                                                id="cv-genre",
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
                                        md=4,
                                    ),
                                    dbc.Col(
                                        [
                                            html.Label(
                                                "L'incident a-t-il été signalé ?",
                                                className="filter-label",
                                            ),
                                            dcc.Dropdown(
                                                id="cv-signale",
                                                options=[
                                                    {
                                                        "label": "Non, c'est la première déclaration",
                                                        "value": "non",
                                                    },
                                                    {
                                                        "label": "Oui, à la police / gendarmerie",
                                                        "value": "police",
                                                    },
                                                    {
                                                        "label": "Oui, à une association locale",
                                                        "value": "asso",
                                                    },
                                                    {
                                                        "label": "Oui, à un établissement de santé",
                                                        "value": "sante",
                                                    },
                                                ],
                                                placeholder="Indiquer…",
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
                    # ── Section 4 : Détails et besoins ────────────────────
                    html.Div(
                        className="form-card",
                        children=[
                            html.Div(
                                className="form-section-header",
                                children=[
                                    html.Span("04", className="section-number"),
                                    html.Div(
                                        [
                                            html.H4(
                                                "Détails et besoins",
                                                className="section-title",
                                            ),
                                            html.P(
                                                "Ces détails nous permettront de vous orienter vers le soutien le plus adapté.",
                                                className="section-subtitle",
                                            ),
                                        ]
                                    ),
                                ],
                            ),
                            html.Label(
                                "Décrivez brièvement la situation (facultatif)",
                                className="filter-label",
                            ),
                            dbc.Textarea(
                                id="cv-description",
                                placeholder=(
                                    "Décrivez les circonstances de l'incident, les faits importants… "
                                    "Ne partagez que ce que vous êtes à l'aise de partager."
                                ),
                                style={
                                    "minHeight": "130px",
                                    "borderRadius": "8px",
                                    "border": "1.5px solid #D8C9E3",
                                    "fontFamily": "Inter, sans-serif",
                                    "fontSize": "0.95rem",
                                    "padding": "12px 14px",
                                    "width": "100%",
                                    "resize": "vertical",
                                },
                            ),
                            html.Div(style={"height": "20px"}),
                            html.Label(
                                "De quel(s) type(s) de soutien avez-vous besoin ? *",
                                className="filter-label",
                            ),
                            dcc.Checklist(
                                id="cv-besoins",
                                options=[
                                    {"label": f"  {b}", "value": b} for b in BESOINS
                                ],
                                inputStyle={
                                    "marginRight": "8px",
                                    "accentColor": "#8E44AD",
                                },
                                labelStyle={
                                    "display": "block",
                                    "padding": "6px 0",
                                    "fontSize": "0.95rem",
                                    "cursor": "pointer",
                                },
                            ),
                            html.Div(style={"height": "20px"}),
                            html.Label(
                                "Urgence de la situation", className="filter-label"
                            ),
                            dcc.RadioItems(
                                id="cv-urgence",
                                options=[
                                    {
                                        "label": "Pas d'urgence immédiate",
                                        "value": "faible",
                                    },
                                    {
                                        "label": "Besoin d'aide dans les prochains jours",
                                        "value": "moyenne",
                                    },
                                    {
                                        "label": "Situation d'urgence – besoin immédiat",
                                        "value": "haute",
                                    },
                                ],
                                inputStyle={
                                    "marginRight": "8px",
                                    "accentColor": "#8E44AD",
                                },
                                labelStyle={
                                    "display": "block",
                                    "padding": "7px 0",
                                    "fontSize": "0.95rem",
                                    "cursor": "pointer",
                                },
                            ),
                        ],
                    ),
                    html.Div(style={"height": "20px"}),
                    # ── Consentement + envoi ───────────────────────────────
                    html.Div(
                        className="form-card",
                        children=[
                            dcc.Checklist(
                                id="cv-consentement",
                                options=[
                                    {
                                        "label": (
                                            "  J'accepte que mes informations soient utilisées dans le cadre "
                                            "du suivi et de la prise en charge des VBG en Guinée, "
                                            "dans le respect de la confidentialité."
                                        ),
                                        "value": "oui",
                                    }
                                ],
                                inputStyle={
                                    "marginRight": "10px",
                                    "accentColor": "#4A235A",
                                    "width": "16px",
                                    "height": "16px",
                                },
                                labelStyle={
                                    "fontSize": "0.9rem",
                                    "color": "#444",
                                    "lineHeight": "1.5",
                                },
                            ),
                            html.Div(style={"height": "20px"}),
                            html.Div(id="cv-feedback"),
                            html.Div(style={"height": "12px"}),
                            dbc.Button(
                                "Envoyer ma déclaration",
                                id="cv-btn-submit",
                                n_clicks=0,
                                className="btn-primary-vbg",
                            ),
                            html.Div(
                                className="urgency-banner",
                                children=[
                                    html.Strong("En cas de danger immédiat :"),
                                    html.Span("  appelez le "),
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
    Output("cv-identity-fields", "children"),
    Input("cv-anonyme", "value"),
)
def toggle_identity(anonyme):
    if anonyme == "non":
        return dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Prénom", className="filter-label"),
                        dbc.Input(
                            id="cv-prenom",
                            placeholder="Votre prénom",
                            className="form-control",
                        ),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.Label("Nom de famille", className="filter-label"),
                        dbc.Input(
                            id="cv-nom",
                            placeholder="Votre nom",
                            className="form-control",
                        ),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.Label(
                            "Contact (téléphone ou email)", className="filter-label"
                        ),
                        dbc.Input(
                            id="cv-contact",
                            placeholder="Ex : +224 6xx xx xx xx ou email",
                            className="form-control",
                        ),
                    ],
                    md=4,
                ),
            ],
            className="g-3 mt-2",
        )
    return html.P(
        "Mode anonyme activé. Aucune information d'identité ne sera enregistrée.",
        style={
            "color": "#1E8449",
            "fontSize": "0.9rem",
            "marginTop": "12px",
            "fontStyle": "italic",
        },
    )


@callback(
    Output("cv-prefecture", "options"),
    Output("cv-prefecture", "disabled"),
    Input("cv-region", "value"),
)
def update_prefectures(region):
    if not region:
        return [], True
    opts = [{"label": p, "value": p} for p in PREFECTURES.get(region, [])]
    return opts, False


@callback(
    Output("cv-feedback", "children"),
    Output("cv-declarant", "value"),
    Output("cv-anonyme", "value"),
    Output("cv-region", "value"),
    Output("cv-prefecture", "value"),
    Output("cv-quartier", "value"),
    Output("cv-lieu", "value"),
    Output("cv-date", "value"),
    Output("cv-type-violence", "value"),
    Output("cv-relation", "value"),
    Output("cv-age", "value"),
    Output("cv-genre", "value"),
    Output("cv-signale", "value"),
    Output("cv-description", "value"),
    Output("cv-besoins", "value"),
    Output("cv-urgence", "value"),
    Output("cv-consentement", "value"),
    Input("cv-btn-submit", "n_clicks"),
    State("cv-declarant", "value"),
    State("cv-anonyme", "value"),
    State("cv-region", "value"),
    State("cv-prefecture", "value"),
    State("cv-lieu", "value"),
    State("cv-date", "value"),
    State("cv-type-violence", "value"),
    State("cv-besoins", "value"),
    State("cv-urgence", "value"),
    State("cv-consentement", "value"),
    prevent_initial_call=True,
)
def submit_declaration(
    n_clicks,
    declarant,
    anonyme,
    region,
    prefecture,
    lieu,
    date_str,
    type_v,
    besoins,
    urgence,
    consentement,
):
    errors = []
    if not declarant:
        errors.append("Veuillez indiquer si vous êtes victime ou témoin.")
    if not region:
        errors.append("La région est obligatoire.")
    if not prefecture:
        errors.append("La préfecture est obligatoire.")
    if not lieu:
        errors.append("Le lieu de l'incident est obligatoire.")
    if not date_str:
        errors.append("La date de l'incident est obligatoire.")
    if not type_v:
        errors.append("Le type de violence est obligatoire.")
    if not besoins:
        errors.append("Veuillez indiquer au moins un besoin de soutien.")
    if not urgence:
        errors.append("Veuillez indiquer l'urgence de la situation.")
    if not consentement or "oui" not in consentement:
        errors.append("Vous devez accepter les conditions de traitement des données.")

    if errors:
        return (
            dbc.Alert([html.Ul([html.Li(e) for e in errors])], color="danger"),
            *([no_update] * 16),
        )

    # TODO : enregistrement en base via create_case()
    urgence_msg = {
        "haute": "Une équipe vous contactera en priorité dans les 24 heures.",
        "moyenne": "Une équipe vous contactera dans les prochains jours.",
        "faible": "Votre déclaration a bien été enregistrée.",
    }.get(urgence, "")

    success = dbc.Alert(
        [
            html.H5("Déclaration envoyée avec succès", style={"marginBottom": "8px"}),
            html.P(urgence_msg, style={"margin": 0}),
            html.P(
                "Merci pour votre courage. Votre déclaration contribue à la protection des victimes.",
                style={"marginTop": "8px", "opacity": 0.85, "fontSize": "0.9rem"},
            ),
        ],
        color="success",
    )

    return (
        success,
        None,
        "oui",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        [],
    )
