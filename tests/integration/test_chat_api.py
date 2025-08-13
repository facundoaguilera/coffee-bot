import pytest
from fastapi.testclient import TestClient
from src.main import app
from unittest.mock import MagicMock
from src.routers.api import set_chat_service
from src.context.interfaces import IContextRetriever
from src.llm.interfaces import IResponseGenerator
from src.services.chat_service import ChatService
from src.context.vector_context import VectorContextRetriever

client = TestClient(app)

@pytest.mark.integration
def test_chat_con_generator_mockeado():
    with TestClient(app) as client:
        # Creo el mock del generador
        mock_generator = MagicMock(spec=IResponseGenerator)
        mock_generator.generate.return_value = "El Freshpresso se prepara con espresso y jugo de naranja."

        # Creo un retriever
        retriever = MagicMock(spec=VectorContextRetriever)
        retriever.get_context.return_value = (["Fake contexto del Freshpresso"], 0.8)

        # Creo service mockeado
        mock_service = ChatService(retriever, mock_generator)
        set_chat_service(mock_service)

        # Ejecuto test
        response = client.post("/chat/", json={"question": "¿Cómo se prepara un Freshpresso?"})
        assert response.status_code == 200
        data = response.json()
        assert "freshpresso" in data["answer"].lower()

@pytest.mark.demandado
def test_chat_real_respuesta_coherente():
    """
    Test de integración que verifica la respuesta real del bot
    usando el modelo Gemini y el contenido del PDF.

    No se ejecuta por defecto. Ejecutar manualmente con:
        pytest -m demandado
    """
    with TestClient(app) as client:
        response = client.post("/chat/", json={"question": "¿Cómo se prepara un Freshpresso?"})
        assert response.status_code == 200
        data = response.json()
        assert "freshpresso" in data["answer"].lower()
