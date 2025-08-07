from fastapi import APIRouter
from models.models import ChatRequest, ChatResponse
from services.chat_service import ChatService

router = APIRouter()

chat_service: ChatService | None = None

def set_chat_service(service: ChatService):
    global chat_service
    chat_service = service

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
    answer = chat_service.handle_chat(req.question.strip())
    return {"answer": answer}