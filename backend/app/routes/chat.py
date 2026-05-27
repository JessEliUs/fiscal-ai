from fastapi import APIRouter
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

SYSTEM_PROMPT = """Eres FiscalAI, un asistente especializado en el sistema fiscal mexicano.
Ayudas a contribuyentes mexicanos a entender sus obligaciones fiscales según su régimen.

Regímenes que conoces:
- RESICO (Régimen Simplificado de Confianza): NO permite deducciones. Tasa fija del 1-2.5%.
- Régimen de Actividad Empresarial: SÍ permite deducciones con factura (CFDI).
- Asalariados (sueldos y salarios): Deducciones limitadas (honorarios médicos, colegiaturas, hipoteca).
- Arrendamiento: Deducciones por gastos del inmueble.

Reglas importantes:
- Siempre pregunta el régimen fiscal antes de hablar de deducciones.
- Sé preciso, claro y usa lenguaje accesible (no jerga legal excesiva).
- Si no sabes algo con certeza, recomienda consultar a un contador.
- Responde siempre en español.
"""

class ChatRequest(BaseModel):
    message: str
    history: list[dict] = []

class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash-lite",
        system_instruction=SYSTEM_PROMPT,
    )
    history = []
    for msg in req.history:
        history.append({"role": msg["role"], "parts": [msg["content"]]})
    
    chat = model.start_chat(history=history)
    response = chat.send_message(req.message)
    return ChatResponse(response=response.text)
