"""
API JSON publique exposée via le serveur Flask sous-jacent de Dash.
Routes disponibles :
  GET /api/cases  → liste des cas validés
  GET /api/stats  → statistiques agrégées
"""

import json
from flask import Blueprint, jsonify, request

from services.cases_service import get_validated_cases
from services.stats_service import get_stats
from database import get_session

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/cases", methods=["GET"])
def api_cases():
    """Retourne les cas validés (JSON)."""
    db = get_session()
    try:
        year = request.args.get("year", type=int)
        region = request.args.get("region")
        cases = get_validated_cases(db, year=year, region=region)
        return jsonify([c.to_dict() for c in cases])
    finally:
        db.close()


@api_bp.route("/stats", methods=["GET"])
def api_stats():
    """Retourne les statistiques agrégées (JSON)."""
    db = get_session()
    try:
        year = request.args.get("year", type=int)
        region = request.args.get("region")
        stats = get_stats(db, year=year, region=region)
        return jsonify(stats)
    finally:
        db.close()
