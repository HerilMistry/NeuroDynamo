import numpy as np


def extract_features(history):

    variance = np.var(history)
    mean_activity = np.mean(history)
    max_activity = np.max(np.abs(history))

    return np.array([variance, mean_activity, max_activity])