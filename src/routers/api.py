## routers/api.py
from fastapi import APIRouter
from models.models import ChatRequest, ChatResponse


router = APIRouter()

@router.post("/", response_model=ChatResponse,
    summary="Conversar sobre café",
    description="""
Este endpoint permite hacerle una **pregunta en español** al bot sobre temas relacionados solo a café.

El bot:
- Busca fragmentos relevantes en un PDF de recetas de café.
- Genera una respuesta usando la API de Gemini (sdk genai).
""",
    response_description="Respuesta generada por el bot con contexto y score")
async def chat(req: ChatRequest):
    answer = req
    return {"answer": answer}