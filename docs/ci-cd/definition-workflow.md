# Phase préalable
- Ajout des notebooks dans le répertoire notebooks (à faire)
- README corrigé mais revoir la façon de faire (le push n'a pas fonctionné)

# Phase 1
## A faire
- Lister les transformations à intégrer dans le pipeline
- Intégrer dans le pipeline Python
- Création du script Python qui convertit le notebook en pipeline prêt à l'emploi

## Objectif
- Séparation nette : nettoyage qui sera converti en SQL + modélisation en Python

## Bonnes pratiques
- Chaque modification = commit

## Blocs
### Bloc 1 : Refactoring pipeline Python
- Création d'une branche
- Codage de toutes les transormations post test/train dans le pipeline Python
- Test en local
- Si tout fonctionne, push
### Bloc 2 : CI/CD tests + build
- Déclencheur : push
- Lancement des tests
- Validation des tests
- Build (raccordement au main)
### Bloc 3 : CI/CD déploiement

## Evènements déclencheurs
- Push sur dev :
 - Tests + build
 
- Pull request vers main
 - Tests + build
 - Validation humaine avant le déploiement (pour répondre à la question 
 : Quelle stratégie vas-tu adopter pour éviter un déploiement prématuré 
 à chaque push ?) 
 - Si go : déploiement sur Hugging Face Spaces
 
 ## Questions (à supprimer de la définition du worklow une fois clarifiées
- Je ne comprends pas :
Comptes-tu écrire un changelog dans tes commits ?

As-tu prévu de faire des branches spécifiques (ex. feature/pipeline_refactor) ?

Que signifie : "packaging si tu le prévois."

# Phase 2 (SQL)
- Lister toutes les étapes de nettoyage
- Les coder en SQL (Mission optionnelle du Projet 4)
- Création d'un répertoire local SQL dans l'arborescence du Projet 5
- Mise en place PostgreSQL (pas encore appris)
- Démarrrer un contener PostgreSQL
- Appliquer les scripts
- Vérifications du bon fonctionnement

 ## Questions (à supprimer de la définition du worklow une fois clarifiées
- Comment mettre en place des scripts SQL testables ?
- Je ne comprends pas les Questions :
 - As-tu prévu de dockeriser PostgreSQL dans le workflow YAML ?
 - Ou vas-tu utiliser une base cloud préexistante (avec secrets) ?

1🔹 1. Reformule avec tes mots :

La définition du build.
Le build vient après les tests et avant la phase de déploiement.
Concrètement, c'est un assemblage, une préparation et une validation des
fichiers finaux qui servirant au déploiement.
Pour mon projet, c'est ce que je faisais déjà sans le savoir lors de ma préparation
de mes soutenances de projet :
Un zip correctement nommé incluant :
- Mes notebooks - scripts compilés et testés
- Un fichier TOML. Exemple :
name = "projet-4-classifiez-automatiquement-des-informations"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "pandas>=2.2.3,<3.0.0",
    "matplotlib>=3.10.3,<4.0.0",
    "seaborn>=0.13.2,<0.14.0",
    "jupyterlab>=4.4.2,<5.0.0",
    "ipykernel>=6.29.5,<7.0.0",
    "numpy>=2.2.0,<2.3.0",
    "scikit-learn>=1.6.1,<2.0.0",
    "missingno>=0.5.2,<1.0.0",
    "xgboost>=3.0.2,<4.0.0",
    "catboost>=1.2.8,<2.0.0",
    "category-encoders>=2.8.1,<3.0.0",
    "imbalanced-learn>=0.13.0,<0.14.0",
    "shap>=0.48.0,<0.49.0"
]
- Un poetry lock
- Eventuellement un README avec le descriptif des éléments envoyés
, je dirais même que c'est recommandé
- Un .bat ? Je ne suis pas sûr
- J'ai un doute avec le .env parce que jusqu'à mainenant tu m'as aidé avec poetry



Le rôle exact du script de conversion (one-shot).
- Permet d'effectuer automatiquement toutes les transformations
nécessaires dans le ColumnTransformer après le split

Le schéma minimal des étapes du pipeline (tests, build, déploiement).
- Test sur tout le notebook pipeline (run complet)
- Si OK constitution du zip comme expliqué plus haut dans le build
- Deploiement

🔹 2. Décide si tu souhaites :

Mettre des branches nommées (feature/) ou rester simple.
Oui je veux appliquer les Bonne pratiques de suite

Préparer un changelog.
Oui

Prévoir un test automatisé des scripts SQL (même basique).

🔹 3. Note dans un doc de travail :

Ce que tu connais déjà.
- Fondamentaux de git
- Je commence à peine à appréhender le CI/CD, fiches obsidian initiation faites

Ce que tu dois encore apprendre (Hugging Face, PostgreSQL, YAML avancé).


