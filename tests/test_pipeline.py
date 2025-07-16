import numpy as np
from app.models.load_pipeline import load_pipeline

def test_pipeline_predict():
    """
    Vérifie que le pipeline se charge et peut prédire sur un exemple minimal.
    """
    pipeline = load_pipeline()

    # Création d'un array 1 ligne 42 colonnes (nb colonnes entrée pipeline)
    X_test = np.zeros((1, 42))


    y_pred = pipeline.predict(X_test)

    assert isinstance(y_pred, (list, np.ndarray))
    assert len(y_pred) == 1
