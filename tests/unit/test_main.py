import pytest
from fastapi.testclient import TestClient
from src.main import app
from unittest.mock import patch, ANY

client = TestClient(app)

@pytest.mark.unit
def test_docs_swagger_disponible():
    response = client.get("/docs")
    assert response.status_code == 200
    assert "Coffee Bot API" in response.text

@pytest.mark.unit
@patch("src.main.set_chat_service")
@patch("src.main.ChatService")
@patch("src.main.build_index")
def test_lifespan_llama_componentes(mock_build_index, mock_chat_service, mock_set_chat_service,monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "fake-key")

    # Mocks configurados
    mock_build_index.return_value = "vectorizer"
    mock_chat_service.return_value = "service"

    # Lanzar la app
    with TestClient(app) as client:
        response = client.get("/docs")  # Forzamos la ejecución del lifespan

    # Verificaciones
    mock_build_index.assert_called_once()
    mock_chat_service.assert_called_once_with("vectorizer", ANY)
    mock_set_chat_service.assert_called_once_with("service")
