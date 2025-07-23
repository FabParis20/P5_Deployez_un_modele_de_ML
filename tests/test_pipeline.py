import numpy as np
import pandas as pd
from app.models.load_pipeline import get_pipeline
from app.models.dummy_data import DUMMY_DATA

def test_pipeline_predict():
    """
    Teste que le pipeline se charge et prédit correctement sur une ligne simulée.
    """
    pipeline = get_pipeline()

    # Crée un DataFrame avec une ligne à partir du dummy_data
    X_test = pd.DataFrame([DUMMY_DATA])

    # Prédiction
    y_pred = pipeline.predict(X_test)

    # Vérifications
    assert isinstance(y_pred, (np.ndarray, list)), "La prédiction doit être un tableau ou une liste"
    assert len(y_pred) == 1, "La prédiction doit contenir une seule valeur"
    assert y_pred[0] in [0, 1], "La prédiction doit être binaire (0 ou 1)"
