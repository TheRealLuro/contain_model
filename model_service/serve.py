from fastapi import FastAPI
import torch
import torch.nn as nn
import numpy as np

app = FastAPI()

# Define model architecture
model = nn.Sequential(
    nn.Linear(4, 16),
    nn.ReLU(),
    nn.Linear(16, 3)
)

# Load weights
model.load_state_dict(
    torch.load("model/iris_model.pt", map_location=torch.device("gpu" if torch.cuda.is_available() else "cpu"))
)

model.eval()

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True
    }

@app.post("/predict")
def predict(data: dict):

    features = np.array(data["features"], dtype=np.float32)

    tensor = torch.tensor(features).unsqueeze(0)

    with torch.no_grad():
        outputs = model(tensor)
        prediction = torch.argmax(outputs, dim=1).item()

    return {
        "prediction": int(prediction),
        "model": "iris-pytorch-v1"
    }