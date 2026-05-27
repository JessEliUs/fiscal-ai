import { useState } from "react";
import { classifyExpense } from "../api";
import styles from "./Classifier.module.css";

const CATEGORY_ICONS = {
  "Transporte": "🚗",
  "Equipo y tecnología": "💻",
  "Servicios profesionales": "🔧",
  "Oficina y papelería": "📁",
  "Alimentación": "🍽️",
  "Salud": "🏥",
  "Gasto personal": "👤",
};

export default function Classifier() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleClassify() {
    if (!input.trim() || loading) return;
    setLoading(true);
    setResult(null);
    try {
      const data = await classifyExpense(input.trim());
      setResult(data);
    } catch {
      setResult({ error: true });
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h2 className={styles.title}>Clasificador de gastos</h2>
        <p className={styles.subtitle}>Describe un gasto y nuestro modelo ML lo categoriza automáticamente</p>
      </div>
      <div className={styles.inputRow}>
        <input className={styles.input} value={input} onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === "Enter" && handleClassify()}
          placeholder="Ej: factura de gasolina, renta de oficina..." disabled={loading} />
        <button className={styles.btn} onClick={handleClassify} disabled={loading || !input.trim()}>
          {loading ? "..." : "Clasificar"}
        </button>
      </div>
      {result && !result.error && (
        <div className={styles.result}>
          <span className={styles.icon}>{CATEGORY_ICONS[result.category] || "📌"}</span>
          <div>
            <p className={styles.category}>{result.category}</p>
            <p className={styles.confidence}>Confianza: {Math.round(result.confidence * 100)}%</p>
          </div>
        </div>
      )}
      {result?.error && <p className={styles.error}>No se pudo clasificar. ¿Está corriendo el servidor?</p>}
      <div className={styles.examples}>
        <p className={styles.examplesTitle}>Ejemplos rápidos:</p>
        <div className={styles.chips}>
          {["gasolina", "laptop trabajo", "renta oficina", "netflix", "consulta médica"].map(ex => (
            <button key={ex} className={styles.chip} onClick={() => setInput(ex)}>{ex}</button>
          ))}
        </div>
      </div>
    </div>
  );
}
