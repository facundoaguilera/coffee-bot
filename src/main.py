from fastapi import FastAPI
from src.routers.api import router, set_chat_service
from src.context.rag_engine import build_index
from src.services.chat_service import ChatService
from src.llm.gemini_generator import GeminiGenerator
from pathlib import Path
from contextlib import asynccontextmanager
from src.context.vector_context import VectorContextRetriever

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Evento de startup
    pdf_path = Path(__file__).parent / "data" / "coffee-recipes.pdf"
    vectorizer = build_index(str(pdf_path), VectorContextRetriever() )
    service = ChatService(vectorizer, GeminiGenerator())
    set_chat_service(service)
    
    yield  
    
app = FastAPI(
    title="Coffee Bot API",
    description="Conversational AI Bot that responds only about coffee (in Spanish)",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router, prefix="/chat")
