# VBG Guinée

> "Collecter une donnée, c'est reconnaître qu'une victime existe. Analyser ces données, c'est construire le chemin vers sa protection."

Plateforme web de recensement et de visualisation des violences basées sur le genre (VBG) en République de Guinée. Elle centralise les déclarations de victimes et de professionnels de terrain, les soumet à validation, et expose les données agrégées sous forme de statistiques publiques.

## Contexte

En Guinée, 92 % des femmes sont touchées par des VBG et 3 victimes sur 4 ne signalent jamais l'incident. L'absence d'une base de données nationale cohérente rend impossible tout pilotage de politiques publiques fondées sur des preuves. VBG Guinée vise à combler ce manque.


## Ce que fait la plateforme

**Pour les victimes et témoins**
Soumettre une déclaration anonyme ou nominative, indiquer ses besoins (juridique, médical, hébergement…) et son niveau d'urgence. La déclaration est transmise aux associations partenaires pour prise en charge.

**Pour les associations partenaires**
Accéder à un espace sécurisé pour consulter les déclarations en attente, les valider ou les rejeter, et saisir directement des cas observés sur le terrain.

**Pour le public et les institutions**
Consulter les statistiques nationales agrégées (cas validés par région, par type de violence) via le tableau de bord public ou l'API JSON ouverte.


## Pages

| URL | Public | Description |
|---|---|---|
| `/` | Tous | Page d'accueil — contexte et chiffres clés |
| `/statistiques` | Tous | Tableau de bord interactif |
| `/contacter` | Victimes / témoins | Formulaire de déclaration confidentielle |
| `/connexion` | Associations | Authentification |
| `/espace/declarations` | Associations | Gestion des déclarations pending |
| `/espace/signaler` | Associations | Saisie d'un cas professionnel |
| `/api/cases` | Tous | Cas validés en JSON |
| `/api/stats` | Tous | Statistiques agrégées en JSON |

## Stack technique

| Composant | Technologie |
|---|---|
| Interface web | Python / Plotly Dash |
| Base de données | Supabase / PostgreSQL |
| ORM | SQLAlchemy |
| API | Flask (intégré à Dash) |
| Styles | CSS personnalisé (assets/custom.css) |
| Déploiement | Render / Railway (Procfile) |
