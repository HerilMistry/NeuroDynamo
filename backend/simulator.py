import numpy as np


def simulate_network(drug_strength=0.0, steps=1000, dt=0.01):

    w_ee = 10 + drug_strength * 5
    w_ei = 12
    w_ie = 10
    w_ii = 0

    E = 0.1
    I = 0.1

    history = []

    for _ in range(steps):
        dE = -E + np.tanh(w_ee*E - w_ei*I)
        dI = -I + np.tanh(w_ie*E - w_ii*I)

        E += dt * dE
        I += dt * dI

        history.append([E, I])

    return np.array(history)