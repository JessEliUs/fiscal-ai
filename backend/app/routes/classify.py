from fastapi import APIRouter
from pydantic import BaseModel
import pickle, os

router = APIRouter()

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../../model/classifier.pkl")

class ClassifyRequest(BaseModel):
    description: str

class ClassifyResponse(BaseModel):
    category: str
    confidence: float

CATEGORY_LABELS = {
    "transporte": "Transporte",
    "equipo": "Equipo y tecnología",
    "servicios": "Servicios profesionales",
    "oficina": "Oficina y papelería",
    "alimentacion": "Alimentación",
    "salud": "Salud",
    "personal": "Gasto personal",
}

@router.post("/classify", response_model=ClassifyResponse)
async def classify_endpoint(req: ClassifyRequest):
    if not os.path.exists(MODEL_PATH):
        return ClassifyResponse(category="sin_modelo", confidence=0.0)
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    prediction = model.predict([req.description])[0]
    proba = model.predict_proba([req.description]).max()
    label = CATEGORY_LABELS.get(prediction, prediction)
    return ClassifyResponse(category=label, confidence=round(float(proba), 2))
