from fastapi import FastAPI, HTTPException
from app.api.schemas import InputData
from app.api.predict import make_prediction

app = FastAPI()

@app.post("/predict")
def predict(data: InputData):
    try:
        prediction = make_prediction(data)
        return {"prediction": prediction}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
