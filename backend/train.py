import numpy as np
from simulator import simulate_network
from features import extract_features
from sklearn.neural_network import MLPClassifier
import joblib

X = []
y = []

for strength in np.linspace(-1, 1, 400):
    history = simulate_network(strength)
    features = extract_features(history)
    X.append(features)

    if features[0] > 0.05:
        y.append(1)  # Hyperexcitable
    else:
        y.append(0)  # Stable

model = MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=1000)
model.fit(X, y)

joblib.dump(model, "classifier.pkl")

print("Training complete. classifier.pkl saved.")
