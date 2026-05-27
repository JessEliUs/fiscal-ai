# 🇲🇽 FiscalAI

Asistente inteligente para contribuyentes mexicanos. Responde preguntas fiscales según tu régimen y clasifica tus gastos automáticamente con ML.

## ¿Qué hace?

- 💬 **Chat fiscal** — Pregunta sobre RESICO, ISR, deducciones, declaraciones y más
- 🏷️ **Clasificador de gastos** — Describe un gasto y el modelo ML lo categoriza (transporte, equipo, servicios, etc.)
- 🤖 **Powered by** Gemini API + scikit-learn

## Stack

| Capa | Tecnología |
|---|---|
| Frontend | React + Vite + CSS Modules |
| Backend | FastAPI (Python) |
| IA | Google Gemini 2.5 Flash Lite |
| ML | scikit-learn (TF-IDF + Logistic Regression) |
| Deploy | Vercel (frontend) + Render (backend) |

## Cómo correrlo localmente

### 1. Clona el repo
```bash
git clone https://github.com/tu-usuario/fiscalai.git
cd fiscalai
```

### 2. Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # agrega tu GEMINI_API_KEY
python model/train.py           # entrena el clasificador ML
uvicorn app.main:app --reload
```

Obtén tu API key gratis en [aistudio.google.com](https://aistudio.google.com) → Get API key.

### 3. Frontend
```bash
cd frontend
npm install
cp .env.example .env            # ya tiene http://localhost:8000/api por defecto
npm run dev
```

Abre `http://localhost:5173` 🚀

## Deploy propio

### Backend en Render
1. Crea un nuevo **Web Service** apuntando a la carpeta `backend/`
2. Build command: `pip install -r requirements.txt && python model/train.py`
3. Start command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
4. Variables de entorno:
   - `GEMINI_API_KEY` → tu API key de Gemini
   - `ALLOWED_ORIGINS` → `https://tu-app.vercel.app`

### Frontend en Vercel
1. Importa el repo y selecciona la carpeta `frontend/` como root
2. Variables de entorno:
   - `VITE_API_URL` → `https://tu-backend.onrender.com/api`
3. Deploy — Vercel detecta Vite automáticamente

## Sobre el modelo ML

El clasificador fue entrenado con scikit-learn usando TF-IDF + Logistic Regression sobre descripciones de gastos en español. Clasifica en 7 categorías: transporte, equipo, servicios, oficina, alimentación, salud y personal.

## Construido en

Next Byte Hacks V2 — 2026
