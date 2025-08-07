from fastapi import FastAPI
from pathlib import Path
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
        
    yield  
    
app = FastAPI(
    title="Coffee Bot API",
    description="Conversational AI Bot that responds only about coffee (in Spanish)",
    version="1.0.0",
    lifespan=lifespan
)

