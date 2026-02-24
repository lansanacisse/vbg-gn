"""
Configuration Supabase et paramètres de l'application.
Copiez ce fichier en .env et renseignez vos vraies valeurs.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ── Supabase ──────────────────────────────────────────────────────────────────
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://xxxx.supabase.co")
SUPABASE_DB_URL = os.getenv(
    "SUPABASE_DB_URL",
    "postgresql://postgres:<PASSWORD>@db.<PROJECT_REF>.supabase.co:5432/postgres"
)

# ── Application ───────────────────────────────────────────────────────────────
APP_TITLE = "VBG Guinée"
APP_SECRET_KEY = os.getenv("APP_SECRET_KEY", "change-me-in-production")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
PORT = int(os.getenv("PORT", 8050))

# ── Données de référence ──────────────────────────────────────────────────────
REGIONS = [
    "Conakry", "Kindia", "Boké", "Labé",
    "Mamou", "Faranah", "Kankan", "N'Zérékoré"
]

TYPES_VIOLENCE = [
    "Violence physique",
    "Violence sexuelle",
    "Violence psychologique",
    "Violence économique",
    "Mariage précoce/forcé",
    "Mutilation génitale féminine",
    "Autre",
]
