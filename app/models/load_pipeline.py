from pathlib import Path
import joblib

def load_pipeline():
    model_path = Path(__file__).parent / "pipeline.joblib"
    pipeline = joblib.load(model_path)
    return pipeline
