This repository contains a computational neuroscience tool that leverages the LLaMA 3.1 model to automatically interpret the results of Wilson-Cowan neural simulations.

By passing extracted simulation features and machine learning classifications into an LLM, this script generates concise, scientific explanations of neural dynamics, focusing on excitation-inhibition balance, stability, and clinical relevance.

Features
Automated Interpretation: Translates raw simulation metrics (variance, mean activity, max activity) into readable scientific insights.

State Classification Analysis: Evaluates ML-predicted state labels to assess the risk of seizure-like dynamics under various drug perturbation strengths.

High-Speed Inference: Uses Groq's API for ultra-fast, low-latency LLM responses.

Prerequisites
Python 3.7+

A Groq API Key

Installation
Clone the repository:

Bash
git clone https://github.com/YourUsername/YourRepoName.git
cd YourRepoName
Install the required dependencies:

Bash
pip install requests
Security Setup: Set up your environment variables. To prevent leaking your credentials, never hardcode your API key directly into the script. Export it directly in your terminal:

Bash
# On Linux/macOS/Git Bash
export GROQ_API_KEY="your_actual_api_key_here"

# On Windows PowerShell
$env:GROQ_API_KEY="your_actual_api_key_here"
Note: If you use a .env file and python-dotenv to manage keys locally, ensure that .env is listed in your .gitignore file before pushing to GitHub.

Usage
Import the explain_state function into your main simulation pipeline and pass the required parameters from your Wilson-Cowan engine.

Python
from your_module_name import explain_state

# Example simulation outputs
state_label = "Hyperexcitable"
drug_strength = 0.5
extracted_features = [0.04, 0.85, 0.98] # [Variance, Mean activity, Max activity]

# Generate the scientific explanation
explanation = explain_state(state_label, drug_strength, extracted_features)
print(explanation)
