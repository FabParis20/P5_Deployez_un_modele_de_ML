import pandas as pd
from app.models.load_pipeline import get_pipeline
from app.api.schemas import InputData

def make_prediction(data: InputData) -> int:
    pipeline = get_pipeline()
    input_df = pd.DataFrame([data.dict()])
    prediction = pipeline.predict(input_df)
    return int(prediction[0])
