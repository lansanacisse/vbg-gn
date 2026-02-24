# 🟣 VBG Guinée

> **Plateforme nationale de recensement des violences basées sur le genre en Guinée**

*"Collecter une donnée, c'est reconnaître qu'une victime existe. Analyser ces données, c'est construire le chemin vers sa protection."*

---

## Présentation

**VBG Guinée** est une application web institutionnelle permettant de :

- Recenser les cas de violences basées sur le genre (VBG) en Guinée
- Visualiser les données via un tableau de bord interactif
- Soumettre de nouveaux cas via un formulaire sécurisé
- Exposer les données validées via une API JSON publique

---

## Architecture

```
vbg_guinee/
├── app.py              ← Application Dash principale + routage
├── config.py           ← Configuration (lue depuis .env)
├── database.py         ← Connexion SQLAlchemy → Supabase
├── models.py           ← Modèles ORM (Association, Case)
├── api.py              ← Blueprint Flask : /api/cases & /api/stats
├── services/
│   ├── cases_service.py  ← CRUD des cas
│   └── stats_service.py  ← Agrégations statistiques
├── pages/
│   ├── dashboard.py    ← Page tableau de bord
│   └── submit_case.py  ← Formulaire de signalement
├── init_db.sql         ← Script SQL d'initialisation Supabase
├── requirements.txt
├── Procfile            ← Pour Render / Railway
└── .env.example        ← Modèle de variables d'environnement
```

---

## Prérequis

- Python 3.11+
- Un projet [Supabase](https://supabase.com) (gratuit)

---

## Installation locale

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-org/vbg-guinee.git
cd vbg-guinee

# 2. Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer les variables d'environnement
cp .env.example .env
# Éditez .env avec vos vraies valeurs Supabase

# 5. Lancer l'application
python app.py
```

Accédez à http://localhost:8050

---

## Connexion à Supabase

### Étape 1 – Créer un projet Supabase

1. Rendez-vous sur [supabase.com](https://supabase.com) → **New project**
2. Choisissez un nom, un mot de passe fort, et la région `West EU` (proche de la Guinée)
3. Attendez ~2 minutes que le projet s'initialise

### Étape 2 – Récupérer la chaîne de connexion

Dans votre projet Supabase :
- **Project Settings** → **Database** → **Connection string** → onglet **URI**
- Copiez l'URI et remplacez `[YOUR-PASSWORD]` par le mot de passe créé à l'étape 1

```
postgresql://postgres:MonMotDePasse@db.xxxxxxxxxxxx.supabase.co:5432/postgres
```

Collez cette valeur dans votre `.env` sous `SUPABASE_DB_URL`.

### Étape 3 – Initialiser les tables

1. Dans Supabase, allez dans **SQL Editor**
2. Copiez-collez le contenu de `init_db.sql`
3. Cliquez **Run** → les tables `associations` et `cases` sont créées avec des données de démo

---

## API publique

L'API retourne uniquement les cas avec `status = 'validated'`.

| Endpoint | Description | Paramètres |
|---|---|---|
| `GET /api/cases` | Liste des cas validés | `?year=2024&region=Conakry` |
| `GET /api/stats` | Statistiques agrégées | `?year=2024&region=Conakry` |

### Exemple de réponse `/api/stats`

```json
{
  "total_cases": 42,
  "by_region": {
    "Conakry": 18,
    "Kindia": 7,
    "N'Zérékoré": 12
  },
  "by_type": {
    "Violence physique": 15,
    "Violence sexuelle": 10,
    "Mariage précoce/forcé": 8
  }
}
```

---

## Déploiement

### Sur Render (recommandé, gratuit)

1. Créez un compte sur [render.com](https://render.com)
2. **New** → **Web Service** → connectez votre dépôt GitHub
3. Configurez :
   - **Runtime** : `Python 3`
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `gunicorn app:server --bind 0.0.0.0:$PORT --workers 2`
4. Ajoutez les variables d'environnement dans **Environment** :
   - `SUPABASE_DB_URL`
   - `APP_SECRET_KEY`
   - `DEBUG=false`
5. Cliquez **Create Web Service** → votre app est en ligne !

### Sur Railway

1. Créez un compte sur [railway.app](https://railway.app)
2. **New Project** → **Deploy from GitHub repo**
3. Ajoutez les variables d'environnement dans l'onglet **Variables**
4. Railway détecte automatiquement le `Procfile` et déploie

---

## Sécurité

- La clé `service_role` Supabase n'est **jamais** exposée au frontend
- L'API publique ne retourne que les cas `validated`
- Les insertions passent toutes par le backend Python (statut `pending` forcé)
- Activez **Row Level Security (RLS)** dans Supabase pour un contrôle fin (voir commentaires dans `init_db.sql`)

---

## Personnalisation

| Fichier | Ce que vous pouvez modifier |
|---|---|
| `config.py` | Listes des régions et types de violence |
| `pages/dashboard.py` | Couleurs, graphiques, mise en page |
| `pages/submit_case.py` | Champs du formulaire, validations |
| `models.py` | Schéma de données (ajouter des colonnes) |

---

## Licence

Ce projet est développé dans un but humanitaire et institutionnel.  
Libre d'utilisation pour les ONG, gouvernements et organisations de protection.
