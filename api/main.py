from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class PredictionRequest(BaseModel):
    features: list

@app.get("/")
def home():
    return {
        "message": "Main API running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/predict")
def predict(data: PredictionRequest):

    response = requests.post(
        "http://model-service:8001/predict",
        json={
            "features": data.features
        }
    )

    return response.json()