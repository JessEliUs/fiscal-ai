# 🇲🇽 FiscalAI

Asistente inteligente para contribuyentes mexicanos. Responde preguntas fiscales según tu régimen y clasifica tus gastos automáticamente.

## ¿Qué hace?

- 💬 **Chat fiscal** — Pregunta sobre RESICO, ISR, deducciones, declaraciones y más
- 🏷️ **Clasificador de gastos** — Describe un gasto y el modelo ML lo categoriza (transporte, equipo, servicios, etc.)
- 🤖 **Powered by** Gemini API + scikit-learn

## Stack

| Capa | Tecnología |
|---|---|
| Frontend | React + Vite + Tailwind |
| Backend | FastAPI (Python) |
| IA | Google Gemini 1.5 Flash |
| ML | scikit-learn (TF-IDF + Logistic Regression) |
| Deploy | Vercel + Render |

## Cómo correrlo localmente

### Backend
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env   # agrega tu GEMINI_API_KEY
python model/train.py  # entrena el clasificador
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Sobre el modelo ML

El clasificador de gastos fue entrenado con scikit-learn usando TF-IDF + Logistic Regression. Clasifica descripciones de gastos en categorías: transporte, equipo, servicios, oficina, alimentación, salud y personal.

## Construido en

Next Byte Hacks V2 — 2025
