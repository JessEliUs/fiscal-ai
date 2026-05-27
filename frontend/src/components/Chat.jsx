import { useState, useRef, useEffect } from "react";
import { sendMessage } from "../api";
import styles from "./Chat.module.css";

function Message({ role, content }) {
  return (
    <div className={`${styles.message} ${role === "user" ? styles.user : styles.assistant}`}>
      <div className={styles.bubble}>
        {content.split("\n").map((line, i) => (
          <span key={i}>{line}{i < content.split("\n").length - 1 && <br />}</span>
        ))}
      </div>
    </div>
  );
}

export default function Chat() {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "¡Hola! Soy FiscalAI 🇲🇽\n\nPuedo ayudarte con tus dudas fiscales: deducciones, regímenes, declaraciones y más. ¿En qué régimen fiscal estás?" }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  async function handleSend() {
    if (!input.trim() || loading) return;
    const userMsg = { role: "user", content: input.trim() };
    const newMessages = [...messages, userMsg];
    setMessages(newMessages);
    setInput("");
    setLoading(true);
    try {
      const history = newMessages.slice(0, -1).map(m => ({
        role: m.role === "assistant" ? "model" : "user",
        content: m.content,
      }));
      const response = await sendMessage(userMsg.content, history);
      setMessages(prev => [...prev, { role: "assistant", content: response }]);
    } catch {
      setMessages(prev => [...prev, { role: "assistant", content: "Hubo un error al conectar. ¿Está corriendo el servidor?" }]);
    } finally {
      setLoading(false);
    }
  }

  function handleKey(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  }

  return (
    <div className={styles.container}>
      <div className={styles.messages}>
        {messages.map((m, i) => <Message key={i} role={m.role} content={m.content} />)}
        {loading && (
          <div className={`${styles.message} ${styles.assistant}`}>
            <div className={`${styles.bubble} ${styles.typing}`}>
              <span /><span /><span />
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>
      <div className={styles.inputArea}>
        <textarea
          className={styles.input}
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={handleKey}
          placeholder="Escribe tu pregunta fiscal... (Enter para enviar)"
          rows={2}
          disabled={loading}
        />
        <button className={styles.sendBtn} onClick={handleSend} disabled={loading || !input.trim()}>
          Enviar
        </button>
      </div>
    </div>
  );
}
