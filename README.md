# Déploiement du modèle de prédiction du turnover — Phase 1 : Pipeline et PostgreSQL

## 📚 Sommaire
- [🎯 Objectif](#-objectif)
- [🧠 Étapes clés](#-étapes-clés)
- [🗄️ Base PostgreSQL](#️-base-postgresql)
- [🧪 Tests & CI/CD](#-tests--cicd)
- [📁 Arborescence du dépôt](#-arborescence-du-dépôt)
- [🚀 Phase 2 : API et Déploiement](#-phase-2--api-et-déploiement)
- [📂 Documentation complémentaire](#-documentation-complémentaire)

---

## 🎯 Objectif

Cette première phase du projet vise à :
- développer un modèle de prédiction du départ volontaire des employés (turnover),
- structurer le pipeline de traitement (préparation + modèle XGBoost),
- **traduire toutes les étapes de traitement en SQL** pour une exécution en base PostgreSQL.

---

## 🧠 Étapes clés

- Analyse exploratoire et feature engineering dans des notebooks Python
- Entraînement d’un modèle XGBoost encapsulé dans un pipeline Scikit-learn (`pipeline.joblib`)
- Sauvegarde des colonnes d’entrée du pipeline (`columns.json`)
- **Reproduction en SQL** des étapes de nettoyage, fusion, transformation
- Construction de la base PostgreSQL avec :
  - `dataset_final` : table d’entrée du modèle
  - `historique_predictions` : journalisation des prédictions

---

## 🗄️ Base PostgreSQL

La base locale comprend deux tables principales :
- `dataset_final` : données nettoyées et transformées à partir de plusieurs fichiers CSV
- `historique_predictions` : enregistrement horodaté de chaque prédiction produite en phase 2

L’ensemble des scripts SQL (création, jointures, transformation, export) est disponible dans le dossier `sql/`.

---

## 🧪 Tests & CI/CD

Un dépôt GitHub distant est utilisé pour :
- Gérer le versionnement du code (`main`, `dev`)
- Déclencher un pipeline CI sur chaque `push` ou `pull_request` avec GitHub Actions
- Exécuter des tests unitaires (prédiction sur données simulées)

### 🔧 Workflow CI/CD (`.github/workflows/ci.yml`)

- `push` ou `pull_request` sur `main` ou `dev` :
  - `checkout` du code source
  - Installation de Python 3.11
  - Installation des dépendances avec Poetry (avec cache)
  - Exécution des tests unitaires Pytest
  - Construction du dossier `build` :
    - `app/`
    - `README.md`
    - `pyproject.toml`
  - Upload du build comme artifact GitHub

---

## 📁 Arborescence du dépôt

| Dossier/Fichier                     | Rôle                                                                 |
|------------------------------------|----------------------------------------------------------------------|
| `notebooks/`                       | Analyse exploratoire et pipeline (`P4_EDA_FE_final`, `P4_Pipeline_ML_final`) |
| `app/models/`                      | Chargement du pipeline, fichiers `pipeline.joblib`, `load_pipeline.py` |
| `sql/`                             | Scripts SQL pour la base de données                                 |
| `docs/`                            | Documentation métier et technique                                   |
| `tests/`                           | Test unitaire du pipeline                                           |
| `.github/workflows/ci.yml`        | Configuration de l'intégration continue (CI)                        |
| `pyproject.toml` / `poetry.lock`  | Dépendances gérées avec Poetry                                      |

---

## 🚀 Phase 2 : API et Déploiement

L’API FastAPI, les tests d'intégration et le déploiement sont traités dans un **second dépôt** :

📁 `projet-5-deploiement-classification-turn-over-fastapi`

Ce dépôt **actuel** se concentre sur :
- la production d’un pipeline **reproductible** et **traçable**
- la mise en place d’une base **PostgreSQL** exploitable par l’API

---

## 📂 Documentation complémentaire

- 🧪 [Standards de code et pratiques ML](docs/README-standards.md)
- ⚙️ [Workflow CI/CD](docs/ci-cd/definition-workflow.md)
- 🧱 [Schéma relationnel PostgreSQL](docs/sql/schema_base_donnees.md)
