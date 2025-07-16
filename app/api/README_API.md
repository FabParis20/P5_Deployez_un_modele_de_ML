# 🎯 API de Prédiction - Modèle de Machine Learning

Cette API expose un point d'entrée pour prédire le risque de départ des employés à partir de données structurées.

---

## 🚀 Endpoint principal

- **POST** `/predict`
- **Description** : Prend en entrée un enregistrement JSON avec toutes les variables attendues, retourne la prédiction.

---

## 📥 Données d'entrée attendues

**Format JSON**

Les données doivent contenir **64 variables numériques**, transformées selon le pipeline d'entraînement :

### 🧩 Variables numériques normalisées (MinMaxScaler)

- revenu_mensuel
- age
- annee_experience_totale
- annees_dans_l_entreprise
- annees_dans_le_poste_actuel
- annes_sous_responsable_actuel
- nombre_participation_pee
- ratio_stagnation
- ratio_sous_responsable
- age_revenu
- satisfaction_moyenne
- interaction_satisfaction_anciennete
- taux_de_formation
- interaction_distance_heures_sup
- surmenage_transports
- revenu_stable
- distance_domicile_travail
- nb_formations_suivies
- delta_eval_x_revenu_stable
- delta_evaluation
- nombre_experiences_precedentes
- annees_depuis_la_derniere_promotion
- frequence_deplacement_num
- augmentation_salaire_precedente

### 🧩 Variables catégorielles (OneHotEncoder)

*(liste des 28 colonnes OneHot)*  
[**Astuce :** Vous pouvez retrouver la liste complète dans `feature_names.py`]

---

### 🧩 Variables ordinales

- niveau_education
- satisfaction_employee_environnement
- note_evaluation_precedente
- niveau_hierarchique_poste
- satisfaction_employee_nature_travail
- satisfaction_employee_equipe
- satisfaction_employee_equilibre_pro_perso
- note_evaluation_actuelle
- frequence_deplacement

---

### 🧩 Variables binaires

- genre_binaire
- heures_supplementaires_binaire
- heures_supplementaires_binaire_passthrough

---

## ⚠️ Validation

Avant prédiction, la pipeline vérifie que :

- Toutes les colonnes attendues sont présentes.
- Les formats sont numériques (float ou int).
- Aucune colonne supplémentaire n'est transmise.

---

## 🧪 Exemple de payload JSON

```json
{
  "revenu_mensuel": 5000,
  "age": 38,
  "annee_experience_totale": 15,
  "...": "...",
  "heures_supplementaires_binaire": 1,
  "heures_supplementaires_binaire_passthrough": 1
}
```

(Pour l'intégralité des colonnes, se référer à feature_names.py.)

## ✅ Réponse

```json
{
  "prediction": 1,
  "probability": 0.87
}
```
## 📂 Référence

Le mapping complet des colonnes est documenté dans :
/app/utils/feature_names.py
