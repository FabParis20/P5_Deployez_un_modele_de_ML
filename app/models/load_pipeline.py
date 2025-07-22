import joblib
from pathlib import Path

_pipeline = None  # cache global

def get_pipeline():
    global _pipeline
    if _pipeline is None:
        model_path = Path(__file__).resolve().parent / "pipeline.joblib"
        if not model_path.exists():
            raise FileNotFoundError(f"Le fichier pipeline.joblib est introuvable à l'emplacement : {model_path}")
        _pipeline = joblib.load(model_path)
    return _pipeline
