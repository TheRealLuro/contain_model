# Containerized AI Model System (Docker + FastAPI + PyTorch)

## How to run
be in the root ./contain_model then, 
- docker-compose up --build

## If you want to train model
go to CONTAIN_MODEL/model_service

cd model_service

python train_model.py

---

## System Architecture
Client → API (:8000) → Model Service (:8001) → prediction
                ↓
           /health checks

---

## Part 1 — Answers

### Model Pulled
ai/smollm2

### What endpoint does it expose?
http://localhost:12434/engines/llama.cpp/v1/chat/completions

### What was the response to your test query?
> Test query - hello

- Reponse: Hello, I'm happy to assist you. What can I help you with today?


# END POINTS

## Model

Base URL:
http://localhost:8001

Health Check:
GET http://localhost:8001/health

Prediction Endpoint:
POST http://localhost:8001/predict

Example Request Body:
{
  "features": [5.1, 3.5, 1.4, 0.2]
}

Example Response:
{
  "prediction": 0,
  "model": "iris-pytorch-v1"
}

---

## API

Base URL:
http://localhost:8000

Health Check:
GET http://localhost:8000/health

Prediction Endpoint:
POST http://localhost:8000/predict

Example Request Body:
{
  "features": [5.1, 3.5, 1.4, 0.2]
}

Example Response:
{
  "prediction": 0,
  "model": "iris-pytorch-v1"
}

---

## Frontend

Frontend URL:
http://localhost:3000

Frontend Behavior:
- User enters 4 Iris feature values
- Frontend sends request to:
  http://localhost:8000/predict
- Displays predicted flower type in UI with the model name there too. 


