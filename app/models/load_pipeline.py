import joblib
from app.utils.binary_mapper import BinaryMapper

def load_pipeline():
    """
    Charge le pipeline ML sauvegardé.
    """
    pipeline = joblib.load("C:/Users/Fab/Documents/P5_Déployez_un_modèle_de_Machine_Learning/app/models/pipeline.joblib")
    return pipeline
