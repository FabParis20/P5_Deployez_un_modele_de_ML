import joblib
import os

def load_pipeline():
    """
    Charge le pipeline ML sauvegardé.
    """
    # Chemin vers le fichier du pipeline
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pipeline_path = os.path.join(current_dir, "pipeline.joblib")

    # Charger le pipeline
    pipeline = joblib.load(pipeline_path)

    return pipeline
