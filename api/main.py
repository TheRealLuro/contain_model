from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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