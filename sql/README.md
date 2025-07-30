# 📘 Étape 4 – Scripts SQL pour la base de données PostgreSQL

Ce dossier contient les scripts SQL utilisés pour :

- Créer la base de données et les tables relationnelles à partir des fichiers bruts (`sirh`, `evaluations_annuelles`, `sondage_bien_etre`)
- Fusionner les données et reproduire les transformations du pipeline Python en SQL
- Exporter un dataset final compatible avec le modèle `pipeline.joblib`
- Gérer la traçabilité des prédictions (inputs/outputs enregistrés en base)

---

## 📁 Contenu des scripts

| Fichier                          | Rôle                                                               |
|----------------------------------|--------------------------------------------------------------------|
| `01_create_tables.sql`           | Crée les tables `sirh`, `evaluations_annuelles`, `sondage_bien_etre` |
| `02_insert_data.sql`             | Insère les données brutes (via `COPY`, `INSERT` ou ORM)           |
| `03_joins_fusion.sql`            | Joint les 3 tables pour produire une table fusionnée de travail   |
| `04_feature_engineering.sql`     | Applique les transformations (encodages, ratios, dérivées, etc.)  |
| `05_export_final.sql`            | Génère la table finale `dataset_pipeline_final` et/ou exporte en CSV |
| `06_register_inputs_outputs.sql` | Crée les tables d’enregistrement des inputs et outputs du modèle  |

---

## 🧪 Exécution recommandée

Ces scripts doivent être exécutés **dans l'ordre indiqué ci-dessus**, soit :

- Via pgAdmin (interface SQL)
- Via `psql` (en ligne de commande)
- Ou traduits en Python avec SQLAlchemy (`app/db/...`)

---

## 📦 Connexion PostgreSQL

Assurez-vous que PostgreSQL est bien installé en local.

**Paramètres par défaut** recommandés pour `.env` ou `config.py` :

```env
DB_NAME=p5_classification
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

```

> 🔎 Pour la documentation détaillée du schéma relationnel, voir docs/sql/schema_base_donnees.md.
