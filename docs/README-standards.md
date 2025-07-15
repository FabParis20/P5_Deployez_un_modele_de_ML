# 📝 Standards de code et pratiques Machine Learning

Ce document décrit les conventions et bonnes pratiques appliquées dans ce projet.

---

## 🏷️ Conventions de branches Git

- **main** : branche de production.
- **dev** : branche de développement.
- **feature/** : branches pour le développement de nouvelles fonctionnalités.
  - Exemple : `feature/pipeline-refactor`
- **hotfix/** : branches pour les corrections urgentes.
  - Exemple : `hotfix/fix-missing-values`

---

## 📝 Conventions de commits

- Utiliser des messages clairs et explicites.
- Structure recommandée :
```<type>: <description>```

**Types proposés :**
- `feat`: ajout d'une nouvelle fonctionnalité
- `fix`: correction d'un bug
- `docs`: modifications de documentation
- `test`: ajout ou modification de tests
- `refactor`: amélioration du code sans modification fonctionnelle
- `chore`: tâches diverses (mise à jour dépendances, etc.)

**Exemple :**

```feat: ajout du pipeline complet dans scikit-learn```


---

## ⚙️ Standards de codage Python

- Respecter **PEP8**.
- Utiliser **black** pour le formatage automatique.
- Documenter les fonctions principales avec des docstrings.
- Organiser le code en modules clairs :
  - `app/api/` : endpoints FastAPI
  - `app/models/` : chargement du pipeline ML
  - `app/utils/` : fonctions utilitaires
  - `sql/` : scripts SQL éventuels

---

## 🧪 Pratiques de test

- Les tests sont écrits avec **Pytest**.
- Chaque fonctionnalité importante doit avoir au moins un test unitaire.
- Un test minimal est requis pour vérifier :
  - Le chargement du pipeline ML.
  - La production d'une prédiction sur un exemple.

> **À compléter :**
> La granularité et le périmètre exact des tests seront précisés après implémentation.

---

## ⚙️ Workflow CI/CD

- Utilisation de **GitHub Actions**.
- Déclencheurs :
  - Push sur `dev` : tests et build.
  - Pull Request vers `main` : tests, build et validation manuelle avant déploiement.
- Le déploiement cible est **Hugging Face Spaces**.

---

## 🛡️ Gestion des environnements

- **development** : environnement de test.
- **production** : environnement de déploiement.
- Les secrets (API keys, credentials) sont gérés via **GitHub Secrets**.

---

## 📝 Mise à jour du présent document

> Ce document est une version initiale.
> 
> **Il sera complété** après :
> - Le choix final des options de tests et de leur granularité.
> - La rédaction précise des cas de test.
> - La validation finale du pipeline CI/CD.
