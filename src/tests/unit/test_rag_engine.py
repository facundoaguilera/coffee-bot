import pytest
from src.context.rag_engine import load_pdf_chunks, build_index
from src.context.vector_context import VectorContextRetriever
from pathlib import Path

@pytest.mark.unit
def test_load_pdf_chunks_devuelve_lista():
    pdf_path = Path(__file__).parent.parent.parent / "src" / "data" / "coffee-recipes.pdf"
    chunks = load_pdf_chunks(str(pdf_path), chunk_size=200)
    assert isinstance(chunks, list) #en chunks se obtiene una lista
    assert all(isinstance(c, str) for c in chunks) #cada fragmento es un string
    assert len(chunks) > 0 #hay chunks

@pytest.mark.unit
def test_build_index_entrena_vectorizer():
    pdf_path = Path(__file__).parent.parent.parent / "src" / "data" / "coffee-recipes.pdf"
    retriever = build_index(str(pdf_path), VectorContextRetriever())
    context, score = retriever.get_context("¿Cómo se hace el espresso?")
    assert isinstance(context, str)
    assert isinstance(score, float)
