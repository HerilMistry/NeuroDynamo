import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def explain_state(state_label, drug_strength, features):

    prompt = f"""
You are a computational neuroscience expert.

Wilson-Cowan neural simulation results:

Drug perturbation strength: {drug_strength}

Extracted features:
Variance: {features[0]}
Mean activity: {features[1]}
Max activity: {features[2]}

ML classification: {state_label}

Explain:
1. Neural stability implications
2. Excitation-inhibition balance
3. Risk of seizure-like dynamics
4. Clinical relevance

Be concise and scientific.
"""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "system", "content": "You are a neuroscience expert."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2,
            "max_tokens": 300,
        },
    )

    result = response.json()
    return result["choices"][0]["message"]["content"]
