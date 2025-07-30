# 🎯 Schéma relationnel textuel (PostgreSQL) – Projet 5

Ce schéma décrit les relations SQL mises en place pour reproduire les étapes de nettoyage et de feature engineering initialement codées en Python.


## 🟦 Table `sirh` (source brute RH)

| Nom colonne                        | Type SQL     | Contraintes / Remarques           |
|-----------------------------------|--------------|------------------------------------|
| id_employee                       | INTEGER      | PRIMARY KEY                        |
| age                               | INTEGER      | NOT NULL                           |
| genre                             | VARCHAR(1)   | NOT NULL – valeurs attendues : 'M', 'F' |
| revenu_mensuel                    | INTEGER      | NOT NULL                           |
| statut_marital                    | VARCHAR(15)  | Exemples : 'Marié(e)', 'Célibataire'   |
| departement                       | VARCHAR(50)  |                                    |
| poste                             | VARCHAR(50)  |                                    |
| nombre_experiences_precedentes    | INTEGER      |                                    |
| nombre_heures_travailless         | INTEGER      |                                    |
| annee_experience_totale           | INTEGER      |                                    |
| annees_dans_l_entreprise          | INTEGER      |                                    |
| annees_dans_le_poste_actuel       | INTEGER      |                                    |

## 🟨 Table `evaluations_annuelles`

| Nom colonne                                 | Type SQL     | Contraintes / Remarques                                                |
|--------------------------------------------|--------------|-------------------------------------------------------------------------|
| satisfaction_employee_environnement         | INTEGER      |                                                                         |
| note_evaluation_precedente                  | INTEGER      |                                                                         |
| niveau_hierarchique_poste                   | INTEGER      |                                                                         |
| satisfaction_employee_nature_travail        | INTEGER      |                                                                         |
| satisfaction_employee_equipe                | INTEGER      |                                                                         |
| satisfaction_employee_equilibre_pro_perso   | INTEGER      |                                                                         |
| eval_number                                 | VARCHAR(10)  | Contient `id_employee` avec préfixe `E_` à nettoyer et convertir en INT |
| note_evaluation_actuelle                    | INTEGER      |                                                                         |
| heure_supplementaires                       | VARCHAR(3)   | Valeurs attendues : 'Oui' / 'Non' à encoder ensuite                    |
| augementation_salaire_precedente            | VARCHAR(10)  | Valeurs : '11 %', '0 %' → à nettoyer et transformer en float ou binaire |

> 🛠️ **Important** : La colonne `eval_number` remplace `id_employee` mais nécessite un nettoyage (suppression du préfixe `E_`) et une conversion en `INTEGER`.  
> Ce champ sera ensuite utilisé comme clé étrangère pour la jointure avec `sirh`.


## 🟩 Table `sondage_bien_etre`

| Nom colonne                              | Type SQL     | Contraintes / Remarques                                                    |
|------------------------------------------|--------------|-----------------------------------------------------------------------------|
| a_quitte_l_entreprise                    | VARCHAR(3)   | Cible du modèle (label) – à encoder en binaire ('Oui' / 'Non')             |
| nombre_participation_pee                 | INTEGER      |                                                                             |
| nb_formations_suivies                    | INTEGER      |                                                                             |
| nombre_employee_sous_responsabilite      | INTEGER      |                                                                             |
| code_sondage                             | INTEGER      | Clé de jointure vers `sirh.id_employee` (à vérifier / renommer si besoin)  |
| distance_domicile_travail                | INTEGER      |                                                                             |
| niveau_education                         | INTEGER      | Variable ordinale (niveaux de diplôme codés de 1 à 4)                       |
| domaine_etude                            | VARCHAR(50)  | Exemples : 'Infra & Cloud', 'Transformation Digitale', 'Autre'             |
| ayant_enfants                            | VARCHAR(1)   | Toujours 'Y' → colonne supprimée dans le pipeline                          |
| frequence_deplacement                    | VARCHAR(20)  | Valeurs textuelles ('Occasionnel', 'Fréquent', ...) → encodage ordinal     |
| annees_depuis_la_derniere_promotion      | INTEGER      |                                                                             |
| annes_sous_responsable_actuel            | INTEGER      |                                                                             |

> 🛠️ **Note** : La jointure avec `sirh` se fera via `code_sondage`, qui correspond à `id_employee`. Une vérification de correspondance exacte est nécessaire avant jointure.



## 🔁 Relations entre les tables

Les trois tables sources seront reliées à partir de clés (explícites ou à nettoyer) permettant d'identifier les employés de façon unique.

- `sirh.id_employee` → **clé primaire**
- `evaluations_annuelles.eval_number` → **doit être nettoyée** (`E_` supprimé, castée en `INTEGER`) pour correspondre à `sirh.id_employee`
- `sondage_bien_etre.code_sondage` → **correspond directement** à `sirh.id_employee` 

## 🟪 Table `dataset_pipeline_final`

> 📁 **Fichier correspondant (pipeline Python)** : `data/employes_net_refacto.csv`  
> 🧮 Colonnes : 37 variables, dont :
> - Transformations numériques (`genre_binaire`, `age_revenu`, etc.)
> - Encodages (`tranche_age`, `frequence_deplacement_num`, etc.)
> - Variables dérivées (`interaction_satisfaction_anciennete`, `taux_de_formation`, etc.)

