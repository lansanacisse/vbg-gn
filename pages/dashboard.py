"""
Page Dashboard – visualisations des cas VBG validés.
"""

import dash
import plotly.graph_objects as go

dash.register_page(__name__, path="/statistiques", title="Statistiques – VBG Guinée", order=1)
import plotly.express as px
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc

from config import REGIONS
from services.stats_service import get_stats
from database import get_session

PRIMARY = "#4A235A"
ACCENT = "#8E44AD"
CARD_BG = "#FFFFFF"


def layout():
    years = list(range(2018, 2026))
    return html.Div(
        [
            # ── Hero
            html.Div(
                className="hero",
                children=[
                    html.H1("VBG Guinée"),
                    html.P(
                        "Plateforme nationale de recensement des violences basées sur le genre"
                    ),
                    html.Blockquote(
                        "\u201cCollecter une donn\u00e9e, c\u2019est reconna\u00eetre qu\u2019une victime existe. "
                        "Analyser ces donn\u00e9es, c\u2019est construire le chemin vers sa protection.\u201d"
                    ),
                ],
            ),
            # ── Filtres
            html.Div(
                className="filters-section",
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Label("Ann\u00e9e", className="filter-label"),
                                    dcc.Dropdown(
                                        id="filter-year",
                                        options=[{"label": "Toutes", "value": "all"}]
                                        + [
                                            {"label": str(y), "value": y}
                                            for y in reversed(years)
                                        ],
                                        value="all",
                                        clearable=False,
                                    ),
                                ],
                                md=4,
                            ),
                            dbc.Col(
                                [
                                    html.Label("R\u00e9gion", className="filter-label"),
                                    dcc.Dropdown(
                                        id="filter-region",
                                        options=[{"label": "Toutes", "value": "Toutes"}]
                                        + [{"label": r, "value": r} for r in REGIONS],
                                        value="Toutes",
                                        clearable=False,
                                    ),
                                ],
                                md=4,
                            ),
                            dbc.Col(
                                [
                                    html.Div(
                                        id="kpi-total", style={"marginTop": "22px"}
                                    ),
                                ],
                                md=4,
                            ),
                        ],
                        className="g-3",
                    ),
                ],
            ),
            # ── Graphiques
            html.Div(
                className="charts-section",
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                [html.Div(id="chart-region", className="chart-card")],
                                md=7,
                            ),
                            dbc.Col(
                                [html.Div(id="chart-type", className="chart-card")],
                                md=5,
                            ),
                        ],
                        className="g-3",
                    ),
                ],
            ),
        ]
    )


@callback(
    Output("kpi-total", "children"),
    Output("chart-region", "children"),
    Output("chart-type", "children"),
    Input("filter-year", "value"),
    Input("filter-region", "value"),
)
def update_dashboard(year, region):
    db = get_session()
    try:
        y = None if year == "all" else int(year)
        r = None if region == "Toutes" else region
        stats = get_stats(db, year=y, region=r)
    finally:
        db.close()

    kpi = html.Div(
        className="kpi-card",
        children=[
            html.P("Cas valid\u00e9s", className="kpi-label"),
            html.H2(stats["total_cases"], className="kpi-value"),
        ],
    )

    by_region = stats["by_region"]
    if by_region:
        fig = px.bar(
            x=list(by_region.keys()),
            y=list(by_region.values()),
            labels={"x": "R\u00e9gion", "y": "Nombre de cas"},
            title="Cas par r\u00e9gion",
            color_discrete_sequence=[ACCENT],
        )
        fig.update_layout(
            paper_bgcolor=CARD_BG,
            plot_bgcolor=CARD_BG,
            font={"family": "Inter, sans-serif"},
            title_font_color=PRIMARY,
            margin=dict(t=44, b=12, l=12, r=12),
        )
        chart_region = dcc.Graph(figure=fig, config={"displayModeBar": False})
    else:
        chart_region = html.P(
            "Aucune donn\u00e9e.",
            style={"color": "#999", "padding": "32px", "textAlign": "center"},
        )

    by_type = stats["by_type"]
    if by_type:
        colors = [
            PRIMARY,
            ACCENT,
            "#C0392B",
            "#1A5276",
            "#117A65",
            "#7D6608",
            "#512E5F",
        ]
        fig2 = go.Figure(
            go.Pie(
                labels=list(by_type.keys()),
                values=list(by_type.values()),
                hole=0.4,
                marker={"colors": colors[: len(by_type)]},
            )
        )
        fig2.update_layout(
            paper_bgcolor=CARD_BG,
            font={"family": "Inter, sans-serif"},
            title="Type de violence",
            title_font_color=PRIMARY,
            margin=dict(t=44, b=12, l=12, r=12),
            legend={"orientation": "v", "font": {"size": 11}},
        )
        chart_type = dcc.Graph(figure=fig2, config={"displayModeBar": False})
    else:
        chart_type = html.P(
            "Aucune donn\u00e9e.",
            style={"color": "#999", "padding": "32px", "textAlign": "center"},
        )

    return kpi, chart_region, chart_type
