const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api";

export async function sendMessage(message, history) {
  const res = await fetch(`${BASE_URL}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, history }),
  });
  if (!res.ok) throw new Error("Error al conectar con el servidor");
  const data = await res.json();
  return data.response;
}

export async function classifyExpense(description) {
  const res = await fetch(`${BASE_URL}/classify`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ description }),
  });
  if (!res.ok) throw new Error("Error al clasificar gasto");
  return await res.json();
}
