import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://xxxx.supabase.co")
SUPABASE_DB_URL = os.getenv(
    "SUPABASE_DB_URL",
    "postgresql://postgres:<PASSWORD>@db.<PROJECT_REF>.supabase.co:5432/postgres",
)

APP_TITLE = "VBG Guinée"
APP_SECRET_KEY = os.getenv("APP_SECRET_KEY", "change-me-in-production")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
PORT = int(os.getenv("PORT", 8050))


REGIONS = [
    "Conakry",
    "Kindia",
    "Boké",
    "Labé",
    "Mamou",
    "Faranah",
    "Kankan",
    "N'Zérékoré",
]


PREFECTURES = {
    "Conakry": ["Kaloum", "Dixinn", "Matam", "Ratoma", "Matoto"],
    "Kindia": ["Kindia", "Coyah", "Dubréka", "Forécariah", "Télimélé"],
    "Boké": ["Boké", "Boffa", "Fria", "Gaoual", "Koundara"],
    "Labé": ["Labé", "Koubia", "Lélouma", "Mali", "Tougué"],
    "Mamou": ["Mamou", "Dalaba", "Pita"],
    "Faranah": ["Faranah", "Dabola", "Dinguiraye", "Kissidougou"],
    "Kankan": ["Kankan", "Kérouané", "Kouroussa", "Mandiana", "Siguiri"],
    "N'Zérékoré": ["N'Zérékoré", "Beyla", "Guéckédou", "Lola", "Macenta", "Yomou"],
}

TYPES_VIOLENCE = [
    "Violence physique",
    "Violence sexuelle",
    "Violence psychologique",
    "Violence économique",
    "Mariage précoce / forcé",
    "Mutilation génitale féminine",
    "Autre",
]

RELATIONS_AUTEUR = [
    "Conjoint / Partenaire",
    "Ex-conjoint / Ex-partenaire",
    "Membre de la famille",
    "Voisin",
    "Inconnu",
    "Collègue / Supérieur",
    "Autorité religieuse / traditionnelle",
    "Autre",
]

LIEUX_INCIDENT = [
    "Domicile",
    "Lieu de travail",
    "Espace public / Rue",
    "École / Université",
    "Lieu de culte",
    "Champ / Zone rurale",
    "Autre",
]


BESOINS = [
    "Soutien psychologique",
    "Aide juridique",
    "Hébergement d'urgence",
    "Soins médicaux",
    "Accompagnement social",
    "Information sur mes droits",
    "Autre",
]


NUMERO_VBG = "116"
NUMERO_POLICE = "117"
