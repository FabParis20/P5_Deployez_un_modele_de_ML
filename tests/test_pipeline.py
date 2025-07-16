import numpy as np
from app.models.load_pipeline import load_pipeline

def test_pipeline_predict():
    """
    Vérifie que le pipeline se charge et peut prédire sur un exemple minimal.
    """
    pipeline = load_pipeline()

    # Exemple factice : adapte le nombre de colonnes si besoin
    X_test = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

    y_pred = pipeline.predict(X_test)

    assert isinstance(y_pred, (list, np.ndarray))
    assert len(y_pred) == 1
