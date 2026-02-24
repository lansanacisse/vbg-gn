# VBG Guinée
## Plateforme nationale de recensement des Violences Basées sur le Genre

> *"Collecter une donnée, c'est reconnaître qu'une victime existe. Analyser ces données, c'est construire le chemin vers sa protection."*

**Dossier de présentation** — À destination des associations, ONG, institutions partenaires et bailleurs de fonds

---

## Contexte et problématique

### Les violences basées sur le genre en Guinée

Les violences basées sur le genre (VBG) constituent l'une des violations des droits humains les plus répandues en République de Guinée. Elles touchent des femmes, des hommes et des enfants dans toutes les régions du pays, dans les milieux urbains comme ruraux, quelle que soit la situation économique ou sociale des victimes.

Malgré leur ampleur, ces violences restent largement sous-documentées. Les victimes hésitent à se signaler par crainte du jugement social, par méconnaissance de leurs droits ou par manque de structures de recueil accessibles et fiables. Les acteurs de terrain collectent des données de manière fragmentée et non centralisée, rendant impossible toute vision nationale cohérente.

### Chiffres clés

| Indicateur | Estimation |
|---|---|
| Femmes victimes non signalées | 3 sur 4 |
| Régions sans suivi centralisé | 8 sur 8 |
| Part des cas de violence conjugale | +60% |
| Victimes de mariage précoce | ~30% |

*Sources : estimations UNFPA Guinée, OMS, rapports associatifs 2022-2023*

### Les principaux défis identifiés

- Absence d'une base de données nationale unique sur les cas de VBG
- Données dispersées entre associations locales, services médicaux et forces de l'ordre
- Manque d'outils accessibles pour les victimes souhaitant signaler un incident
- Impossibilité pour les décideurs de piloter des politiques publiques fondées sur des preuves
- Stigmatisation et obstacles culturels qui freinent les signalements

> *"Sans données fiables, il est impossible de concevoir des politiques de protection efficaces. Chaque cas non signalé est une victime invisible pour le système."*

---

## La solution — Plateforme VBG Guinée

### Une plateforme numérique nationale et ouverte

VBG Guinée est une plateforme web développée pour centraliser, visualiser et rendre accessible l'ensemble des données relatives aux violences basées sur le genre en République de Guinée. Elle s'adresse simultanément à trois types d'utilisateurs : les professionnels de terrain, les victimes et témoins, et les décideurs.

### Trois espaces distincts, une seule plateforme

**📊 Tableau de bord public**
Visualisations interactives des données validées : répartition par région, types de violence, tendances dans le temps. Accessible à tous, sans inscription.

**📝 Signalement professionnel**
Formulaire sécurisé pour les acteurs de terrain (associations, ONG, services sociaux) pour enregistrer de nouveaux cas de manière standardisée.

**🤝 Espace victimes**
Formulaire bienveillant et confidentiel pour les victimes et témoins directs, avec orientation vers des structures d'aide et affichage permanent des numéros d'urgence.

### Fonctionnalités clés

**Tableau de bord analytique**
- Nombre total de cas validés
- Répartition par région (graphique en barres)
- Répartition par type de violence (graphique camembert)
- Filtres dynamiques par année et région
- Mise à jour automatique en temps réel

**Formulaire de déclaration victime**
- Mode anonyme activé par défaut
- 4 sections : identité, géolocalisation, contexte de violence, besoins
- Niveau d'urgence sélectionnable (faible / moyen / critique)
- Checklist des besoins : juridique, médical, hébergement, psychologique…
- Numéros d'urgence affichés en permanence (116, 117)

**API de données ouverte**
- Accès aux cas validés au format JSON
- Statistiques agrégées par région et par type
- Filtrage par année et région
- Compatible avec tout outil d'analyse (Excel, R, Python…)

**Sécurité et confidentialité**
- Aucune information personnelle exposée publiquement
- Validation humaine obligatoire avant toute publication
- Données chiffrées en transit (HTTPS/SSL)
- Consentement explicite requis à chaque soumission

---

## Architecture technique

### Stack technologique

| Composant | Technologie | Rôle |
|---|---|---|
| Interface web | Python / Plotly Dash | Pages, graphiques interactifs, formulaires |
| Base de données | Supabase / PostgreSQL | Stockage sécurisé sur le cloud |
| API | Flask (intégré) | Exposition des données en JSON |
| Connexion DB | SQLAlchemy | Interface sécurisée avec la base |
| Hébergement | Render / Railway | Mise en ligne, HTTPS automatique |
| Code source | Open Source (GitHub) | Auditable, réutilisable par d'autres pays |

### Avantages concrets

- Aucun logiciel à installer — accessible depuis tout navigateur web
- Données stockées en sécurité sur des serveurs en Europe
- Coût d'hébergement : 0 à 25 USD/mois selon le trafic
- Prise en main facile — pas besoin d'informaticien pour les opérations courantes
- Code open source — adaptable à d'autres pays ou contextes
- Évolutif — nouvelles fonctionnalités ajoutables sans refonte

---

## Impact attendu et bénéficiaires

### Qui bénéficiera de cette plateforme ?

**👩 Les victimes de VBG**
Accès à un canal de signalement confidentiel, adapté aux non-lettrés et disponible depuis un smartphone. Orientation vers des structures d'aide et numéros d'urgence affichés en permanence.

**🏥 Les associations et ONG de terrain**
Outil standardisé pour enregistrer les cas, les partager au niveau national et contribuer à une base de données commune. Gain de temps dans la collecte et réduction des doublons.

**🏛️ Les institutions et décideurs**
Tableau de bord en temps réel pour piloter les politiques publiques, allouer les ressources de manière ciblée et mesurer l'impact des programmes de lutte contre les VBG.

**🔬 Les chercheurs et journalistes**
API de données publique et ouverte permettant d'accéder aux statistiques validées pour des analyses académiques, des enquêtes ou des rapports d'organisation.

### Objectifs mesurables à 12 mois

| Objectif | Cible |
|---|---|
| Cas enregistrés et validés | 500+ |
| Régions couvertes | 8 / 8 |
| Associations partenaires | 20+ |
| Données publiques et auditables | 100% |

---

## Feuille de route

### Phase 1 — Mois 1 à 3 : Lancement

- Finalisation et tests de la plateforme
- Connexion à la base de données et hébergement en ligne
- Formation de 5 associations pilotes à Conakry
- Collecte des premiers cas et validation des processus
- Communication publique et lancement officiel

### Phase 2 — Mois 4 à 8 : Extension régionale

- Déploiement dans les 7 autres régions administratives
- Formation des associations locales à l'outil
- Ajout d'une carte interactive de la Guinée
- Intégration d'un système de notifications pour les validateurs
- Première publication d'un rapport trimestriel national

### Phase 3 — Mois 9 à 12 : Consolidation

- Ouverture du back-office de gestion aux associations partenaires
- Développement d'un module de rapport PDF automatisé
- Connexion avec des outils partenaires (UNFPA, ONU Femmes…)
- Évaluation d'impact et rapport annuel
- Exploration d'une adaptation dans d'autres pays de la CEDEAO

### Ce dont nous avons besoin

**👥 Réseau d'associations**
20 à 30 associations locales prêtes à alimenter la base de données avec rigueur et régularité.

**🎓 Formation**
Sessions de formation pour les référents de chaque association sur l'utilisation de la plateforme.

**💰 Financement**
Coûts d'hébergement, coordination, communication et animation du réseau partenaire.

---

## Propositions de partenariat

### Comment s'impliquer ?

**Niveau 1 — Association collectrice de données**
Votre équipe enregistre les cas VBG via la plateforme dans votre région.
- Accès à la plateforme et formation offerte
- Vos données contribuent au rapport national
- Visibilité sur le tableau de bord public

**Niveau 2 — Partenaire institutionnel**
Votre organisation contribue à la gouvernance et à la validation des données.
- Accès au back-office de validation
- Co-signature des rapports nationaux
- Accès à l'API complète pour vos propres analyses

**Niveau 3 — Bailleur de fonds / Donateur**
Vous financez tout ou partie du déploiement et de la coordination nationale.
- Rapport d'impact trimestriel dédié
- Logo affiché sur la plateforme publique
- Accès prioritaire aux données et analyses

**Niveau 4 — Partenaire technique**
Vous contribuez au développement de nouvelles fonctionnalités.
- Intégration de vos outils existants via l'API
- Co-développement de modules spécifiques
- Crédit dans la documentation technique

> *"Cette plateforme n'appartient à personne — elle est au service de toutes les victimes. Plus nous serons nombreux à l'alimenter, plus elle deviendra un outil puissant de transformation sociale."*

---

## Contact et prochaines étapes

### Étapes proposées après ce premier contact

1. Prise de contact par email ou téléphone
2. Réunion de présentation (30 à 45 minutes, en ligne ou à Conakry)
3. Démonstration en direct de la plateforme
4. Proposition d'accord de partenariat adapté à vos besoins
5. Intégration et formation de vos équipes

### Coordonnées

| | |
|---|---|
| 📧 Email | contact@vbg-guinee.org |
| 📱 Téléphone / WhatsApp | +224 6XX XX XX XX |
| 🌐 Plateforme web | https://vbg-guinee.onrender.com |
| 📍 Adresse | Conakry, République de Guinée |
| 💻 Code source | github.com/votre-organisation/vbg-guinee |

---

*VBG Guinée — Ensemble, rendons les violences visibles pour mieux les combattre.*

**Urgence VBG : 116  |  Gendarmerie : 117**