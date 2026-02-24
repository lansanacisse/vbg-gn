# 📘 Documentation complète — VBG Guinée
### Guide de prise en main, personnalisation et développement
> **Pour qui ?** Cette documentation est rédigée pour une personne qui n'est pas développeuse professionnelle mais qui souhaite comprendre, modifier et faire évoluer ce projet en toute autonomie.

---

## Table des matières

1. [Comprendre la structure du projet](#1-comprendre-la-structure-du-projet)
2. [Installer et lancer le projet](#2-installer-et-lancer-le-projet)
3. [Créer et connecter la base de données Supabase](#3-créer-et-connecter-la-base-de-données-supabase)
4. [Comprendre le fonctionnement technique](#4-comprendre-le-fonctionnement-technique)
5. [Changer les couleurs](#5-changer-les-couleurs)
6. [Modifier les textes et les listes](#6-modifier-les-textes-et-les-listes)
7. [Ajouter ou modifier un onglet](#7-ajouter-ou-modifier-un-onglet)
8. [Modifier les graphiques du tableau de bord](#8-modifier-les-graphiques-du-tableau-de-bord)
9. [Modifier les formulaires](#9-modifier-les-formulaires)
10. [Comprendre la base de données](#10-comprendre-la-base-de-données)
11. [L'API publique](#11-lapi-publique)
12. [Déployer en ligne](#12-déployer-en-ligne)
13. [Suggestions d'améliorations futures](#13-suggestions-daméliorations-futures)
14. [Glossaire pour non-développeurs](#14-glossaire-pour-non-développeurs)

---

## 1. Comprendre la structure du projet

Voici tous les fichiers du projet et leur rôle expliqué simplement :

```
vbg_guinee/
│
├── app.py                  ← Le "chef d'orchestre" : lance l'appli, gère la navigation
├── config.py               ← Les réglages : couleurs de base, listes de régions, etc.
├── database.py             ← La "passerelle" entre l'appli et Supabase
├── models.py               ← La description des tables en base de données
├── api.py                  ← Les adresses web pour accéder aux données en JSON
│
├── pages/                  ← Chaque fichier = une page de l'application
│   ├── dashboard.py        ← Page "Tableau de bord" avec les graphiques
│   ├── submit_case.py      ← Page "Signaler un cas" (formulaire professionnel)
│   └── contact_victime.py  ← Page "Contacter une association" (formulaire victime)
│
├── services/               ← Le "moteur" : récupère et traite les données
│   ├── cases_service.py    ← Lit et écrit les cas en base de données
│   └── stats_service.py    ← Calcule les statistiques pour les graphiques
│
├── assets/
│   └── custom.css          ← Tout le design visuel (couleurs, espacements, polices)
│
├── init_db.sql             ← Script pour créer les tables dans Supabase
├── requirements.txt        ← Liste des bibliothèques Python nécessaires
├── .env.example            ← Modèle pour vos identifiants Supabase (à copier en .env)
├── Procfile                ← Instructions pour déployer sur Render ou Railway
└── README.md               ← Résumé rapide du projet
```

### Schéma de fonctionnement simplifié

```
Navigateur (utilisateur)
        │
        ▼
   app.py  ←── Reçoit la requête, choisit quelle page afficher
        │
        ├── pages/dashboard.py      → Affiche les graphiques
        ├── pages/submit_case.py    → Affiche le formulaire professionnel
        └── pages/contact_victime.py → Affiche le formulaire victime
                │
                ▼
        services/  ← Demande les données
                │
                ▼
        database.py ← Se connecte à Supabase
                │
                ▼
        Supabase (PostgreSQL) ← Stocke toutes les données
```

---

## 2. Installer et lancer le projet

### Ce dont vous avez besoin

- **Python 3.11 ou plus récent** → [python.org/downloads](https://www.python.org/downloads/)
- **VS Code** (recommandé) → [code.visualstudio.com](https://code.visualstudio.com/)
- Un compte **Supabase** (gratuit) → [supabase.com](https://supabase.com)

### Étape par étape

**1. Télécharger les fichiers**

Placez tous les fichiers dans un dossier `vbg_guinee/` sur votre ordinateur, en respectant exactement la structure ci-dessus (avec les sous-dossiers `pages/`, `services/`, `assets/`).

**2. Ouvrir le projet dans VS Code**

```
Fichier → Ouvrir le dossier → Sélectionner "vbg_guinee"
```

**3. Ouvrir un terminal**

Dans VS Code : `Terminal → Nouveau terminal`

**4. Créer un environnement virtuel** (une sorte de "bac à sable" pour Python)

```bash
python -m venv venv
```

Puis l'activer :
- Sur **Windows** : `venv\Scripts\activate`
- Sur **Mac/Linux** : `source venv/bin/activate`

Vous verrez `(venv)` apparaître dans le terminal — c'est bon signe !

**5. Installer les dépendances**

```bash
pip install -r requirements.txt
```

Attendez que tout s'installe (1-2 minutes).

**6. Configurer vos identifiants Supabase**

Copiez le fichier `.env.example` et renommez la copie `.env` :
```bash
cp .env.example .env
```

Ouvrez `.env` dans VS Code et renseignez vos vraies valeurs (voir section 3).

**7. Lancer l'application**

```bash
python app.py
```

Ouvrez votre navigateur et allez sur : **http://localhost:8050**

---

## 3. Créer et connecter la base de données Supabase

### Étape 1 — Créer un compte et un projet Supabase

1. Allez sur [supabase.com](https://supabase.com) → cliquez **Start your project**
2. Connectez-vous avec GitHub ou créez un compte email
3. Cliquez **New project**
4. Remplissez :
   - **Name** : `vbg-guinee` (ou ce que vous voulez)
   - **Database Password** : choisissez un mot de passe fort et **notez-le** !
   - **Region** : `West EU (Ireland)` — c'est le plus proche de la Guinée
5. Cliquez **Create new project** et attendez ~2 minutes

### Étape 2 — Créer les tables (initialiser la base)

1. Dans votre projet Supabase, cliquez sur **SQL Editor** dans le menu gauche
2. Cliquez **New query**
3. Copiez-collez tout le contenu du fichier `init_db.sql`
4. Cliquez le bouton **Run** (▶️)
5. Vous devriez voir : `Success. No rows returned`

Les tables `associations` et `cases` sont maintenant créées avec des données de démonstration !

**Pour vérifier :** Cliquez sur **Table Editor** dans le menu gauche → vous verrez vos tables avec des données.

### Étape 3 — Récupérer la chaîne de connexion

1. Dans Supabase, allez dans **Project Settings** (icône engrenage en bas à gauche)
2. Cliquez **Database**
3. Descendez jusqu'à **Connection string**
4. Cliquez sur l'onglet **URI**
5. Copiez l'adresse — elle ressemble à :
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.xxxxxxxxxxxx.supabase.co:5432/postgres
   ```
6. Remplacez `[YOUR-PASSWORD]` par votre vrai mot de passe

### Étape 4 — Remplir le fichier .env

Ouvrez votre fichier `.env` et remplissez-le :

```env
SUPABASE_URL=https://xxxxxxxxxxxx.supabase.co
SUPABASE_DB_URL=postgresql://postgres:MonMotDePasse@db.xxxxxxxxxxxx.supabase.co:5432/postgres
APP_SECRET_KEY=une-chaine-aleatoire-longue-et-unique
DEBUG=false
PORT=8050
```

> ⚠️ **Important** : Ne partagez jamais ce fichier `.env`. Il contient vos mots de passe. Le fichier `.gitignore` est configuré pour l'exclure automatiquement de Git.

### Étape 5 — Tester la connexion

Relancez l'application :
```bash
python app.py
```

Si le tableau de bord affiche des données → la connexion fonctionne ! 🎉

---

## 4. Comprendre le fonctionnement technique

Cette section explique comment les pièces s'assemblent, sans jargon inutile.

### Comment une page s'affiche

Quand vous allez sur `http://localhost:8050/signaler`, voici ce qui se passe :

1. **`app.py`** reçoit la visite et regarde l'URL `/signaler`
2. Il appelle la fonction `submit_case.layout()` dans `pages/submit_case.py`
3. Cette fonction construit la page HTML et la renvoie
4. Votre navigateur affiche le résultat

```python
# Dans app.py — c'est le "aiguilleur" :
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/signaler":
        return submit_case.layout()      # → affiche la page formulaire
    if pathname == "/contacter":
        return contact_victime.layout()  # → affiche la page victime
    return dashboard.layout()            # → par défaut : tableau de bord
```

### Comment les graphiques se mettent à jour

Quand vous changez le filtre "Année" sur le tableau de bord :

1. Dash détecte le changement (c'est un **callback**)
2. Il appelle `update_dashboard(year, region)` dans `dashboard.py`
3. Cette fonction interroge la base de données via `get_stats()`
4. Elle crée de nouveaux graphiques et les renvoie
5. La page se met à jour sans rechargement

### Comment les données voyagent

```
Formulaire soumis par l'utilisateur
        ↓
submit_case.py  → valide les champs
        ↓
cases_service.py → crée un objet "Case"
        ↓
database.py → envoie vers Supabase
        ↓
Supabase → sauvegarde en base avec status="pending"
```

---

## 5. Changer les couleurs

Il y a **deux endroits** où les couleurs sont définies. Vous devez les modifier dans les deux.

### Endroit 1 : `assets/custom.css` (ligne 7 à 24)

C'est le fichier CSS — il contrôle 90% du design visuel.

```css
:root {
  --primary:      #4A235A;   ← Violet foncé (navbar, titres, boutons)
  --primary-dark: #341840;   ← Violet encore plus foncé (survol)
  --accent:       #8E44AD;   ← Violet clair (dégradés, liens actifs)
  --accent-light: #C39BD3;   ← Violet très clair (petits éléments)
  --bg:           #F9F7FB;   ← Fond de page (gris très léger)
  --card-bg:      #FFFFFF;   ← Fond des cartes (blanc)
  --text:         #2C2C2C;   ← Texte principal (presque noir)
  --text-muted:   #6B6B6B;   ← Texte secondaire (gris)
  --success:      #1E8449;   ← Messages de succès (vert)
  --danger:       #C0392B;   ← Messages d'erreur (rouge)
}
```

**Exemple : passer en bleu institutionnel**

```css
:root {
  --primary:      #1A3A5C;   ← Bleu marine
  --primary-dark: #0F2238;   ← Bleu très foncé
  --accent:       #2E86C1;   ← Bleu clair
  --accent-light: #AED6F1;   ← Bleu très clair
  --bg:           #F4F8FB;   ← Fond légèrement bleuté
}
```

**Exemple : passer en vert (santé/nature)**

```css
:root {
  --primary:      #1B5E20;   ← Vert foncé
  --primary-dark: #0A3D10;
  --accent:       #388E3C;   ← Vert moyen
  --accent-light: #A5D6A7;   ← Vert pâle
  --bg:           #F1F8F1;
}
```

> 💡 **Trouver des couleurs** : utilisez [coolors.co](https://coolors.co) ou [color-hex.com](https://www.color-hex.com) pour choisir des codes hexadécimaux (#XXXXXX).

### Endroit 2 : `app.py` et les fichiers de pages (lignes avec `PRIMARY` et `ACCENT`)

Les couleurs sont aussi définies directement dans le code Python pour les graphiques Plotly. Cherchez et remplacez :

Dans **`app.py`** (ligne 30-31) :
```python
PRIMARY = "#4A235A"   ← même valeur que --primary dans le CSS
ACCENT  = "#8E44AD"   ← même valeur que --accent dans le CSS
```

Dans **`pages/dashboard.py`** (ligne 14-15) :
```python
PRIMARY  = "#4A235A"
ACCENT   = "#8E44AD"
```

> ⚠️ Ces valeurs doivent être identiques à celles du CSS pour que tout soit cohérent.

---

## 6. Modifier les textes et les listes

### Changer le nom de l'application

Dans **`config.py`** (ligne 19) :
```python
APP_TITLE = "VBG Guinée"   ← changer ici
```

Dans **`app.py`** (ligne 35) :
```python
dbc.NavbarBrand("🟣 VBG Guinée", ...)   ← changer ici aussi
```

### Changer la liste des régions

Dans **`config.py`** (lignes 25-28) :
```python
REGIONS = [
    "Conakry", "Kindia", "Boké", "Labé",
    "Mamou", "Faranah", "Kankan", "N'Zérékoré"
]
```

Ajoutez, retirez ou modifiez les régions entre guillemets, séparées par des virgules.

### Changer la liste des types de violence

Dans **`config.py`** (lignes 30-38) :
```python
TYPES_VIOLENCE = [
    "Violence physique",
    "Violence sexuelle",
    "Violence psychologique",
    "Violence économique",
    "Mariage précoce/forcé",
    "Mutilation génitale féminine",
    "Autre",
]
```

### Changer les préfectures par région

Dans **`pages/contact_victime.py`** (lignes 20-29) :
```python
PREFECTURES = {
    "Conakry":    ["Kaloum", "Dixinn", "Matam", "Ratoma", "Matoto"],
    "Kindia":     ["Kindia", "Coyah", "Dubréka", "Forécariah", "Télimélé"],
    # ... ajoutez vos préfectures ici
}
```

### Changer la citation d'accueil

Dans **`pages/dashboard.py`** (ligne 28-30) :
```python
html.Blockquote(
    "Votre nouvelle citation ici."
),
```

### Changer les textes du hero (grande bannière)

Chaque page a son propre hero. Par exemple dans **`pages/dashboard.py`** :
```python
html.Div(className="hero", children=[
    html.H1("VBG Guinée"),           ← Titre principal
    html.P("Texte sous le titre"),    ← Sous-titre
    html.Blockquote("Citation..."),   ← Citation en italique
]),
```

---

## 7. Ajouter ou modifier un onglet

### Modifier un onglet existant

Dans **`app.py`**, trouvez la section `dbc.Nav([...])` (lignes 38-45) :

```python
dbc.Nav([
    dbc.NavItem(dbc.NavLink("📊 Tableau de bord",          href="/")),
    dbc.NavItem(dbc.NavLink("📝 Signaler un cas",          href="/signaler")),
    dbc.NavItem(dbc.NavLink("🤝 Contacter une association", href="/contacter")),
    dbc.NavItem(dbc.NavLink("🔌 API",                      href="/api/stats")),
], navbar=True, className="ms-auto"),
```

Pour changer le nom d'un onglet, modifiez le texte entre guillemets.
Pour changer l'icône, remplacez l'emoji (copiez-collez depuis [emojipedia.org](https://emojipedia.org)).

### Ajouter un nouvel onglet (exemple : page "À propos")

**Étape 1 : Créer le fichier de la page**

Créez `pages/a_propos.py` :

```python
from dash import html

def layout():
    return html.Div([
        html.Div(className="hero", children=[
            html.H1("À propos"),
            html.P("Description de la plateforme VBG Guinée."),
        ]),
        html.Div(className="form-section", children=[
            html.Div(className="form-card", children=[
                html.H4("Notre mission"),
                html.P("Texte de présentation..."),
            ]),
        ]),
    ])
```

**Étape 2 : Importer la page dans `app.py`**

En haut de `app.py`, ajoutez (ligne 14) :
```python
import pages.a_propos as a_propos
```

**Étape 3 : Ajouter l'onglet dans la navbar**

```python
dbc.NavItem(dbc.NavLink("ℹ️ À propos", href="/a-propos")),
```

**Étape 4 : Ajouter le routage**

Dans la fonction `display_page` de `app.py` :
```python
def display_page(pathname):
    if pathname == "/signaler":
        return submit_case.layout()
    if pathname == "/contacter":
        return contact_victime.layout()
    if pathname == "/a-propos":            ← ajoutez ceci
        return a_propos.layout()           ← et ceci
    return dashboard.layout()
```

### Supprimer un onglet

1. Supprimez la ligne correspondante dans `dbc.Nav([...])`
2. Supprimez la condition correspondante dans `display_page`
3. Vous pouvez aussi supprimer le fichier de la page dans `pages/`

---

## 8. Modifier les graphiques du tableau de bord

Tous les graphiques sont dans **`pages/dashboard.py`** dans la fonction `update_dashboard`.

### Changer le type de graphique des régions

Actuellement c'est un **graphique en barres** (`px.bar`). Vous pouvez le remplacer par :

**Graphique horizontal :**
```python
fig = px.bar(
    x=list(by_region.values()),   ← valeurs sur X
    y=list(by_region.keys()),     ← régions sur Y
    orientation="h",              ← h = horizontal
    title="Cas par région",
    color_discrete_sequence=[ACCENT],
)
```

**Carte choroplèthe (avancé)** : nécessite un fichier GeoJSON de la Guinée.

### Changer les couleurs des graphiques

**Graphique en barres** — une seule couleur :
```python
color_discrete_sequence=["#E74C3C"]   ← rouge, par exemple
```

**Graphique camembert** — plusieurs couleurs :
```python
colors = ["#1A5276", "#2E86C1", "#AED6F1", "#85C1E9", "#5DADE2"]
```

### Ajouter un nouveau graphique (exemple : évolution dans le temps)

Dans la fonction `layout()` de `dashboard.py`, ajoutez une nouvelle carte :

```python
html.Div(className="charts-section", children=[
    dbc.Row([
        dbc.Col([html.Div(id="chart-region",   className="chart-card")], md=7),
        dbc.Col([html.Div(id="chart-type",     className="chart-card")], md=5),
    ], className="g-3"),
    dbc.Row([
        dbc.Col([html.Div(id="chart-timeline", className="chart-card")], md=12),  ← nouveau
    ], className="g-3 mt-3"),
]),
```

Puis dans le callback `update_dashboard`, ajoutez la sortie et le graphique :

```python
@callback(
    Output("kpi-total",     "children"),
    Output("chart-region",  "children"),
    Output("chart-type",    "children"),
    Output("chart-timeline","children"),   ← nouveau
    Input("filter-year",    "value"),
    Input("filter-region",  "value"),
)
def update_dashboard(year, region):
    # ... code existant ...

    # Nouveau graphique — évolution mensuelle
    import pandas as pd
    cases = get_validated_cases(db, year=y, region=r)
    if cases:
        df = pd.DataFrame([{"date": c.date_incident} for c in cases])
        df["mois"] = pd.to_datetime(df["date"]).dt.to_period("M").astype(str)
        monthly = df.groupby("mois").size().reset_index(name="count")
        fig3 = px.line(monthly, x="mois", y="count", title="Évolution mensuelle",
                       color_discrete_sequence=[ACCENT])
        fig3.update_layout(paper_bgcolor=CARD_BG, plot_bgcolor=CARD_BG,
                           font={"family": "Inter, sans-serif"})
        chart_timeline = dcc.Graph(figure=fig3, config={"displayModeBar": False})
    else:
        chart_timeline = html.P("Pas de données.")

    return kpi, chart_region, chart_type, chart_timeline
```

> 💡 Pour utiliser `pandas`, ajoutez `pandas` dans `requirements.txt` et relancez `pip install -r requirements.txt`.

---

## 9. Modifier les formulaires

### Ajouter un champ au formulaire "Signaler un cas"

Dans **`pages/submit_case.py`**, trouvez la section avec les `dbc.Row` et `dbc.Col`.

**Exemple : ajouter un champ "Description"** :

```python
# Après le bloc des 3 colonnes (date/genre/âge), ajoutez :
html.Label("Description (facultatif)", className="filter-label"),
dbc.Textarea(
    id="f-description",
    placeholder="Décrivez brièvement la situation...",
    style={"minHeight": "100px", "borderRadius": "8px",
           "border": "1.5px solid #D8C9E3", "padding": "10px",
           "fontFamily": "Inter, sans-serif", "width": "100%"},
),
html.Div(style={"height": "16px"}),
```

Puis dans le **callback** `submit_case`, ajoutez l'ID dans les `State` :
```python
State("f-description", "value"),
```

Et dans la fonction, récupérez la valeur :
```python
def submit_case(n_clicks, region, prefecture, type_v, date_str, gender, age, description):
```

### Rendre un champ obligatoire

Dans le callback, ajoutez une vérification :
```python
if not description or not description.strip():
    errors.append("La description est obligatoire.")
```

### Changer les options d'un menu déroulant

Trouvez le `dcc.Dropdown` correspondant et modifiez ses `options` :

```python
dcc.Dropdown(
    id="f-gender",
    options=[
        {"label": "Féminin",  "value": "F"},
        {"label": "Masculin", "value": "M"},
        {"label": "Non-binaire", "value": "NB"},   ← ajouter
        {"label": "Préfère ne pas répondre", "value": "NR"},   ← ajouter
    ],
)
```

---

## 10. Comprendre la base de données

### Les deux tables principales

**Table `associations`** — les organisations partenaires :

| Colonne | Type | Description |
|---|---|---|
| `id` | UUID | Identifiant unique (généré automatiquement) |
| `name` | Texte | Nom de l'association |
| `region` | Texte | Région d'intervention |
| `created_at` | Date/heure | Date d'ajout (automatique) |

**Table `cases`** — les cas de VBG :

| Colonne | Type | Description |
|---|---|---|
| `id` | UUID | Identifiant unique |
| `association_id` | UUID | Lien vers l'association (optionnel) |
| `region` | Texte | Région du cas |
| `prefecture` | Texte | Préfecture |
| `type_violence` | Texte | Type de violence |
| `victim_age` | Nombre | Âge de la victime |
| `victim_gender` | Texte | Genre (F, M, Autre) |
| `date_incident` | Date | Date de l'incident |
| `status` | Enum | `pending` / `validated` / `rejected` |
| `created_at` | Date/heure | Date de soumission |

### Le cycle de vie d'un cas

```
Soumission formulaire
        ↓
  status = "pending"   (en attente de validation)
        ↓
  Examen par l'équipe
        ↓
  status = "validated"  → apparaît dans les stats et l'API
  status = "rejected"   → n'apparaît nulle part publiquement
```

### Valider un cas manuellement (dans Supabase)

1. Allez dans **Table Editor** → table `cases`
2. Cliquez sur la ligne du cas à valider
3. Changez la valeur du champ `status` de `pending` à `validated`
4. Cliquez **Save**

### Ajouter une colonne à la base de données

**Exemple : ajouter une colonne `description`**

1. Dans Supabase → **SQL Editor** → **New query** :
```sql
ALTER TABLE cases ADD COLUMN description TEXT;
```
2. Cliquez **Run**

3. Dans `models.py`, ajoutez la colonne (après `date_incident`) :
```python
description = Column(String, nullable=True)
```

4. Dans `to_dict()` de `models.py`, ajoutez :
```python
"description": self.description,
```

### Exporter les données

Dans Supabase → **Table Editor** → cliquez l'icône **Export** → choisissez CSV ou JSON.

---

## 11. L'API publique

L'API permet à d'autres applications de récupérer vos données automatiquement.

### Routes disponibles

| URL | Description |
|---|---|
| `/api/cases` | Liste de tous les cas validés |
| `/api/cases?year=2024` | Cas validés en 2024 |
| `/api/cases?region=Conakry` | Cas validés à Conakry |
| `/api/stats` | Statistiques agrégées |
| `/api/stats?year=2024&region=Kindia` | Stats filtrées |

### Exemple de réponse `/api/stats`

```json
{
  "total_cases": 42,
  "by_region": {
    "Conakry": 18,
    "Kindia": 7
  },
  "by_type": {
    "Violence physique": 15,
    "Violence sexuelle": 10
  }
}
```

### Modifier l'API

L'API est définie dans **`api.py`**. Pour ajouter une nouvelle route :

```python
@api_bp.route("/associations", methods=["GET"])
def api_associations():
    """Retourne la liste des associations."""
    db = get_session()
    try:
        from models import Association
        assocs = db.query(Association).all()
        return jsonify([
            {"id": str(a.id), "name": a.name, "region": a.region}
            for a in assocs
        ])
    finally:
        db.close()
```

Accessible ensuite à `/api/associations`.

---

## 12. Déployer en ligne

### Option A : Render (recommandé, gratuit)

1. Créez un compte sur [render.com](https://render.com)
2. Poussez votre code sur GitHub (créez un dépôt privé)
3. Dans Render : **New** → **Web Service** → connectez votre dépôt GitHub
4. Configurez :
   - **Runtime** : `Python 3`
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `gunicorn app:server --bind 0.0.0.0:$PORT --workers 2`
5. Dans **Environment** (variables d'environnement), ajoutez :
   - `SUPABASE_DB_URL` = votre URL de connexion
   - `APP_SECRET_KEY` = une chaîne aléatoire longue
   - `DEBUG` = `false`
6. Cliquez **Create Web Service**

Votre application sera accessible via une URL du type `https://vbg-guinee.onrender.com`.

> ⚠️ Sur le plan gratuit de Render, l'application "s'endort" après 15 minutes d'inactivité. Le premier chargement peut prendre 30 secondes.

### Option B : Railway

1. Créez un compte sur [railway.app](https://railway.app)
2. **New Project** → **Deploy from GitHub repo**
3. Railway détecte le `Procfile` automatiquement
4. Ajoutez vos variables d'environnement dans l'onglet **Variables**
5. Déployez

### Mettre à jour l'application en ligne

Chaque fois que vous modifiez des fichiers et les poussez sur GitHub, Render ou Railway redéploie automatiquement.

---

## 13. Suggestions d'améliorations futures

Voici une liste de fonctionnalités que vous pourriez ajouter, classées par difficulté.

### 🟢 Facile (modifications simples)

**1. Ajouter un KPI "Cas ce mois-ci"**
- Dans `dashboard.py`, ajoutez une deuxième carte KPI avec un filtre sur le mois en cours
- Très utile pour le suivi mensuel

**2. Ajouter un graphique "Âge moyen des victimes"**
- Calculez la moyenne de `victim_age` dans `stats_service.py`
- Affichez-le comme un indicateur texte

**3. Page "Ressources utiles"**
- Une page statique avec les numéros d'urgence, adresses des associations partenaires, liens vers des ressources légales

**4. Traduction en langues locales**
- Ajouter un sélecteur de langue (Français / Peul / Malinké / Soussou)
- Stocker les traductions dans un dictionnaire Python

**5. Logo dans la navbar**
- Dans `app.py`, remplacez l'emoji `🟣` par une vraie image :
```python
html.Img(src="/assets/logo.png", height="32px"),
```
- Placez votre logo dans `assets/logo.png`

### 🟡 Intermédiaire

**6. Tableau de gestion des cas (back-office)**
- Une page `/admin` protégée par mot de passe
- Affiche tous les cas `pending` avec des boutons "Valider" / "Rejeter"
- Nécessite un système d'authentification simple (Flask-Login ou variable de session)

**7. Export CSV des données**
- Un bouton "Télécharger les données" sur le tableau de bord
- Génère un fichier CSV avec tous les cas validés filtrés
```python
from dash import dcc
dcc.Download(id="download-csv")
```

**8. Carte interactive de la Guinée**
- Afficher les cas sur une carte avec Plotly Mapbox ou Folium
- Chaque région colorée selon le nombre de cas (carte choroplèthe)
- Nécessite un fichier GeoJSON des régions de Guinée

**9. Système de notifications par email**
- Envoyer un email à l'équipe quand un nouveau cas est soumis
- Utiliser `smtplib` (Python) ou le service [Resend](https://resend.com) (gratuit)

**10. Graphique de tendance (courbe dans le temps)**
- Afficher l'évolution du nombre de cas mois par mois
- Très utile pour identifier des périodes à risque

### 🔴 Avancé

**11. Authentification et rôles utilisateurs**
- Créer des comptes (admin, association, lecteur)
- Les associations ne voient que leurs propres cas
- Les admins valident les cas
- Utiliser [Flask-Login](https://flask-login.readthedocs.io/) ou Supabase Auth

**12. Application mobile (PWA)**
- Rendre l'application installable sur smartphone comme une app native
- Ajouter un fichier `manifest.json` dans `assets/`

**13. Rapport PDF automatique**
- Générer un rapport PDF mensuel avec les statistiques
- Utiliser la bibliothèque `reportlab` ou `weasyprint`

**14. Intégration WhatsApp**
- Permettre de signaler un cas par WhatsApp
- Utiliser l'API Twilio pour WhatsApp
- Très utile pour les zones avec connexion limitée

**15. Tableau de bord en temps réel**
- Actualisation automatique des graphiques toutes les X minutes
- Utiliser `dcc.Interval` dans Dash :
```python
dcc.Interval(id="auto-refresh", interval=5*60*1000, n_intervals=0)  # toutes les 5 min
```

---

## 14. Glossaire pour non-développeurs

| Terme | Signification simple |
|---|---|
| **Python** | Le langage de programmation utilisé pour tout le projet |
| **Dash** | La bibliothèque Python qui crée l'interface web interactive |
| **Plotly** | La bibliothèque qui crée les graphiques interactifs |
| **Flask** | Le "serveur web" sous-jacent à Dash, qui gère les requêtes HTTP |
| **Supabase** | Service cloud qui héberge votre base de données PostgreSQL |
| **PostgreSQL** | Le système de gestion de base de données utilisé |
| **SQLAlchemy** | L'outil Python qui parle à la base de données à votre place |
| **CSS** | Le langage qui définit les couleurs, tailles et positions |
| **HTML** | Le langage qui structure le contenu des pages web |
| **API** | Une adresse web qui retourne des données brutes (JSON) au lieu d'une page |
| **JSON** | Format de données lisible par les ordinateurs (et les humains) |
| **UUID** | Identifiant unique généré automatiquement (ex: `a3f8-...`) |
| **Callback** | Fonction qui se déclenche automatiquement quand quelque chose change |
| **Route** | Une URL spécifique qui affiche une page ou retourne des données |
| **ENV / .env** | Fichier qui contient vos mots de passe et clés secrètes |
| **Venv** | Environnement Python isolé pour ce projet (évite les conflits) |
| **Git / GitHub** | Outils pour sauvegarder et partager votre code |
| **Render / Railway** | Services pour mettre votre application en ligne |
| **Gunicorn** | Le serveur web utilisé en production (remplace le serveur de développement) |
| **Bootstrap** | Bibliothèque CSS qui facilite la mise en page responsive |
| **Responsive** | Design qui s'adapte automatiquement à toutes les tailles d'écran |
| **RLS** | Row Level Security — sécurité qui contrôle qui peut lire/écrire dans Supabase |
| **pending** | Statut d'un cas : en attente de validation |
| **validated** | Statut d'un cas : approuvé, visible dans les stats |
| **rejected** | Statut d'un cas : rejeté, invisible publiquement |

---

## 📞 En cas de problème

### L'application ne démarre pas

Vérifiez que :
1. Vous êtes bien dans le dossier `vbg_guinee/` dans le terminal
2. L'environnement virtuel est activé (`(venv)` visible dans le terminal)
3. Toutes les dépendances sont installées : `pip install -r requirements.txt`
4. Le fichier `.env` existe et est correctement rempli

### "ModuleNotFoundError"

Une bibliothèque manque. Exécutez :
```bash
pip install -r requirements.txt
```

### "Connection refused" ou erreur Supabase

- Vérifiez votre `SUPABASE_DB_URL` dans le fichier `.env`
- Vérifiez que votre projet Supabase est actif (pas en pause)
- Vérifiez que le mot de passe dans l'URL est correct

### Les graphiques sont vides

- Allez dans Supabase → Table Editor → vérifiez que des cas ont le `status = 'validated'`
- Exécutez le script `init_db.sql` si les tables sont vides

### Le CSS ne se charge pas

- Vérifiez que le fichier `custom.css` est bien dans le dossier `assets/`
- Le dossier doit s'appeler exactement `assets` (minuscules)

---

*Documentation rédigée pour VBG Guinée — Plateforme nationale de recensement des VBG*
*Dernière mise à jour : 2024*