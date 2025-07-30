# 📝 Standards de code et pratiques Machine Learning

Ce document décrit les conventions et bonnes pratiques appliquées dans ce projet.

---

## 🏷️ Conventions de branches Git

- **main** : branche de production.
- **dev** : branche de développement.
- **feature/** : branches pour le développement de nouvelles fonctionnalités.
  - Exemple : feature/pipeline-refactor
- **hotfix/** : branches pour les corrections urgentes.
  - Exemple : hotfix/fix-missing-values

**Exemple de création de branche fonctionnelle :**
```bash
git checkout -b feature/ajout-endpoint
git push origin feature/ajout-endpoint
```

---

## 📝 Conventions de commits

- Utiliser des messages clairs et explicites.
- Structure recommandée :
```
<type>: <description>
```

- Possibilité de lier un numéro d’issue si nécessaire :
fix: corrige l'erreur de prédiction (#42)

**Types proposés :**
- feat: ajout d'une nouvelle fonctionnalité
- fix: correction d'un bug
- docs: modifications de documentation
- test: ajout ou modification de tests
- refactor: amélioration du code sans modification fonctionnelle
- chore: tâches diverses (mise à jour dépendances, etc.)

**Exemple :**
```bash
✅ test(pipeline): ajout d’un test minimal de prédiction
🐛 fix(model): suppression d’une feature mal encodée
```


---

## ⚙️ Standards de codage Python

- Respecter PEP8.
- Utiliser black pour le formatage automatique.
  black .
- (Optionnel) Utiliser isort pour trier les imports.
  isort .
- Documenter les fonctions principales avec des docstrings.
- Organiser le code en modules clairs :
  - app/api/ : endpoints FastAPI
  - app/models/ : chargement du pipeline ML
  - app/utils/ : fonctions utilitaires
  - sql/ : scripts SQL éventuels

---

🧪 Pratiques de test

Les tests sont écrits avec Pytest.

Un test minimal est fourni dans ce dépôt pour vérifier :
- Le chargement du pipeline ML (`get_pipeline()`)
- La capacité du pipeline à effectuer une prédiction à partir d’un `DataFrame` conforme

📌 Les tests liés à l’API FastAPI (erreurs 404, prédiction via endpoint, enregistrement en BDD, etc.) sont décrits dans le dépôt dédié à la phase 2.


