# 📄 Définition du Workflow CI/CD – Projet 5

## 🎯 Objectif du Workflow

Mettre en place un pipeline CI/CD complet qui :

- Vérifie la qualité et la cohérence du code à chaque modification.
- Exécute automatiquement les tests unitaires.
- Prépare les artefacts nécessaires au déploiement.
- Déploie la solution sur Hugging Face Spaces après validation manuelle.

---

## 🛠️ Outils et technologies utilisés

- **GitHub Actions** – orchestrateur du pipeline.
- **Poetry** – gestion des dépendances et de l’environnement Python.
- **Pytest** – exécution des tests automatiques.
- **Hugging Face Spaces** – plateforme cible de déploiement.
- **Git** – gestion des branches et des versions.

---

## 🪝 Événements déclencheurs

Le pipeline se déclenche dans les cas suivants :

1. **Push sur la branche `dev`**
   - Exécution des tests automatiques.
   - Vérification de la build.
   - Pas de déploiement automatique.

2. **Pull Request vers la branche `main`**
   - Exécution des tests automatiques.
   - Vérification de la build.
   - Validation manuelle obligatoire avant fusion.
   - Si validation, déclenchement du déploiement automatique sur Hugging Face Spaces.

---

## 🏷️ Branches utilisées

- `main` : branche de production (stable).
- `dev` : branche de développement.
- `feature/*` : branches spécifiques aux nouvelles fonctionnalités ou refactorings.
- `hotfix/*` : branches de correction.

---

## ⚙️ Étapes du pipeline

Le pipeline comprend les étapes suivantes :

### 1️⃣ Tests automatiques

- Installation de l’environnement avec Poetry.
- Lancement de Pytest.
- Génération d’un rapport de test.

### 2️⃣ Build

- Préparation de l’environnement prêt au déploiement.

> **À surveiller :**
>
> Le build pourra consister à constituer un ZIP incluant :
> - Le pipeline sauvegardé.
> - Le code de l’API.
> - La configuration Poetry.
> - Le README.
> 
> **Cependant**, sur Hugging Face Spaces, le build peut être implicite (le dépôt Git devient directement la source du déploiement).  
> Il faudra vérifier à l’étape de configuration YAML si un packaging manuel est réellement nécessaire.

### 3️⃣ Déploiement

- Déploiement automatique après validation manuelle de la Pull Request.
- Utilisation des secrets GitHub pour gérer les credentials.

---

## 🔐 Environnements et secrets

- **Environnements GitHub :**
  - `development` (tests).
  - `production` (déploiement).

- **Secrets attendus :**
  - Variables de connexion à Hugging Face Spaces.
  - (Optionnel) Credentials PostgreSQL si nécessaire plus tard.

---

## ✅ Conditions de succès

- Tous les tests Pytest passent sans erreur.
- La build est exempte de warnings critiques.
- La validation manuelle de la Pull Request est réalisée avant le déploiement.
- Le pipeline s’exécute en moins de 10 minutes.

---

## 📝 Standards de code et pratiques ML

Un README spécifique décrira :

- Les conventions de nommage des branches et des commits.
- Les bonnes pratiques de versioning.
- La structuration des scripts Python et SQL.
- Les règles de validation des données.

> **À surveiller :**
>
> Ce README des standards est prévu mais pas encore rédigé.  
> Il devra être finalisé avant de considérer l’étape CI/CD totalement close.

---

## 🧪 Granularité des tests

Actuellement, le pipeline prévoit des tests Pytest globaux.

> **À surveiller :**
>
> Il faudra détailler précisément :
> - Les cas de test à implémenter (même un test minimal).
> - La vérification du chargement du pipeline.
> - La vérification de la prédiction sur un exemple.

---

## 🧭 Prochaines étapes

1. Rédiger le README des standards.
2. Créer un YAML minimal de test du pipeline.
3. Étendre le YAML avec les étapes de build et de déploiement.
4. Configurer les secrets et environnements sur GitHub.
5. Rédiger les premiers tests unitaires.
6. Valider l’exécution complète du pipeline.

---

## 🔗 Références et documentation

- [GitHub Actions Documentation](https://docs.github.com/actions)
- [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Pytest Documentation](https://docs.pytest.org/)
