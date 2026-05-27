import { useState } from "react";
import Chat from "./components/Chat";
import Classifier from "./components/Classifier";
import styles from "./App.module.css";

export default function App() {
  const [tab, setTab] = useState("chat");
  return (
    <div className={styles.app}>
      <header className={styles.header}>
        <div className={styles.logo}>
          <span className={styles.logoIcon}>🇲🇽</span>
          <span className={styles.logoText}>FiscalAI</span>
        </div>
        <nav className={styles.nav}>
          <button className={`${styles.navBtn} ${tab === "chat" ? styles.active : ""}`} onClick={() => setTab("chat")}>
            💬 Asistente
          </button>
          <button className={`${styles.navBtn} ${tab === "classify" ? styles.active : ""}`} onClick={() => setTab("classify")}>
            🏷️ Clasificar gasto
          </button>
        </nav>
      </header>
      <main className={styles.main}>
        {tab === "chat" ? <Chat /> : <Classifier />}
      </main>
    </div>
  );
}
