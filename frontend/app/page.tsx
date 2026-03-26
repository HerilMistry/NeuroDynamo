"use client";

import { useState } from "react";
import axios from "axios";
import styles from "./page.module.css";

export default function Home() {

  const [strength, setStrength] = useState(0);
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const runSimulation = async () => {
    setLoading(true);
    const res = await axios.get(
      `http://127.0.0.1:8000/simulate?drug_strength=${strength}`
    );
    setResult(res.data);
    setLoading(false);
  };

  const getStateClass = () => {
    if (!result) return styles.neutral;
    return result.state === "Hyperexcitable"
      ? styles.hyper
      : styles.stable;
  };

  return (
    <div className={styles.container}>

      <header className={styles.header}>
        <h1> NeuroDynamics Sandbox</h1>
        <p>Wilson–Cowan Neural Circuit Simulation + ML Stability Analysis</p>
      </header>

      <section className={styles.panel}>
        <h2>Drug Perturbation</h2>

        <div className={styles.sliderRow}>
          <input
            type="range"
            min="-1"
            max="1"
            step="0.05"
            value={strength}
            onChange={(e) => setStrength(parseFloat(e.target.value))}
          />
          <span>{strength.toFixed(2)}</span>
        </div>

        <button
          onClick={runSimulation}
          className={styles.button}
        >
          {loading ? "Simulating..." : "Run Simulation"}
        </button>
      </section>

      {result && (
        <section className={styles.results}>

          <div className={`${styles.badge} ${getStateClass()}`}>
            Brain State: {result.state}
          </div>

          <div className={styles.metrics}>
            <div className={styles.card}>
              <h3>Variance</h3>
              <p>{result.features[0].toFixed(4)}</p>
            </div>

            <div className={styles.card}>
              <h3>Mean Activity</h3>
              <p>{result.features[1].toFixed(4)}</p>
            </div>

            <div className={styles.card}>
              <h3>Max Activity</h3>
              <p>{result.features[2].toFixed(4)}</p>
            </div>
          </div>

          <div className={styles.explanation}>
            <h2>Mechanistic Interpretation</h2>
            <p>{result.explanation}</p>
          </div>

        </section>
      )}

    </div>
  );
}
