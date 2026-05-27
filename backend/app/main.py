from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chat, classify
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="FiscalAI", version="1.0.0")

origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api")
app.include_router(classify.router, prefix="/api")
