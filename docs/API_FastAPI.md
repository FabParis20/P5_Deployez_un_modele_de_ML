# 📘 Documentation technique de l’API FastAPI

## 🔹 URL de l’API

https://fabparis20-projet-5-deploiement-classification-t-7c1b135.hf.space

## 🔹 Documentation interactive Swagger

https://fabparis20-projet-5-deploiement-classification-t-7c1b135.hf.space/docs

## 🧠 Fonctionnalité
Cette API expose un modèle de classification entraîné sur des données RH pour prédire si un employé est susceptible de quitter l’entreprise (`1`) ou de rester (`0`), à partir de ses caractéristiques individuelles et professionnelles.

## 🔁 Endpoint principal
`POST /predict`

Description : Prédiction du turnover à partir des données d’un employé.

Requête : JSON contenant 34 variables (issues du pipeline d’ingénierie des features)

Réponse : JSON `{ "prediction": 0 | 1 }`

## 📝 Exemple de requête
```json
{
  "age": 34,
  "revenu_mensuel": 3500,
  "genre_binaire": 1,
  "statut_marital": "Célibataire",
  "departement": "IT",
  "poste": "Analyste",
  "nombre_experiences_precedentes": 3,
  "annee_experience_totale": 7,
  "annees_dans_l_entreprise": 2,
  "annees_dans_le_poste_actuel": 1,
  "satisfaction_employee_environnement": 3,
  "note_evaluation_precedente": 3,
  "niveau_hierarchique_poste": 4,
  "satisfaction_employee_nature_travail": 2,
  "satisfaction_employee_equipe": 3,
  "satisfaction_employee_equilibre_pro_perso": 3,
  "note_evaluation_actuelle": 3,
  "augementation_salaire_precedente": 0.1,
  "nombre_participation_pee": 1,
  "nb_formations_suivies": 1,
  "annees_depuis_la_derniere_promotion": 1,
  "annes_sous_responsable_actuel": 2,
  "niveau_education": 3,
  "domaine_etude": "Commerce",
  "distance_domicile_travail": 15.0,
  "frequence_deplacement_num": 1,
  "taux_de_formation": 0.3,
  "tranche_age": "Intermédiaire",
  "heures_supplementaires_binaire": 0,
  "age_revenu": 119000.0,
  "interaction_distance_heures_sup": 15.0,
  "interaction_satisfaction_anciennete": 6.0,
  "ratio_sous_responsable": 1.0,
  "ratio_stagnation": 0.2,
  "satisfaction_moyenne": 3.0,
  "surmenage_transports": 0.2
}
```
## ✅ Exemple de réponse
```json
{
  "prediction": 1
}
```
- `1` = l’employé est susceptible de quitter l’entreprise
- `0` = l’employé est susceptible de rester

## 🧱 Technologies utilisées
| Élément        | Outil                                                   |
|----------------|----------------------------------------------------------|
| Framework API  | `FastAPI`                                               |
| Serveur        | `Uvicorn`                                               |
| Modèle ML      | `XGBoostClassifier` dans un pipeline `scikit-learn`     |
| Sérialisation  | `joblib`                                                |
| Validation     | `Pydantic` (`InputData`)                                |
| Déploiement    | Docker + Hugging Face Spaces                            |


## 📎 Limitations et conseils d’utilisation
- Tous les champs sont obligatoires
- Les données doivent respecter les types définis dans InputData
- L’API ne gère pas encore les cas de données manquantes ou mal typées (retournera 422 Unprocessable Entity)
- Swagger est idéal pour tester l’API manuellement avant de l’intégrer dans un front-end ou un automate