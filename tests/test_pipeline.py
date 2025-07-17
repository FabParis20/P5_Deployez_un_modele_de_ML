import numpy as np
import pandas as pd
from app.models.load_pipeline import load_pipeline
from app.models.dummy_data import DUMMY_DATA  # ✅ On importe ici le dictionnaire validé

def test_pipeline_predict():
    """
    Vérifie que le pipeline se charge et peut prédire sur un exemple minimal.
    """
    pipeline = load_pipeline()

    # Construction d’un DataFrame avec une seule ligne de données simulées
    X_test = pd.DataFrame([DUMMY_DATA])

    # Prédiction
    y_pred = pipeline.predict(X_test)

    # Vérifications
    assert isinstance(y_pred, (np.ndarray, list)), "La prédiction doit être un tableau ou une liste"
    assert len(y_pred) == 1, "La prédiction doit contenir une seule valeur"
