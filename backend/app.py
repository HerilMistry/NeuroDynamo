from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from simulator import simulate_network
from features import extract_features
from models import classify
from llm import explain_state

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/simulate")
def run_simulation(drug_strength: float):

    history = simulate_network(drug_strength)
    features = extract_features(history)
    state = classify(features)
    explanation = explain_state(state, drug_strength, features)

    return {
        "state": state,
        "features": features.tolist(),
        "explanation": explanation
    }
