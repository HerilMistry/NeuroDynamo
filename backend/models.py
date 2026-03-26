import joblib
import numpy as np


model = joblib.load("classifier.pkl")


def classify(features):
    prediction = model.predict([features])[0]
    return "Hyperexcitable" if prediction == 1 else "Stable"
