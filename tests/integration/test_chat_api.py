import pytest
from fastapi.testclient import TestClient
from src.main import app
client = TestClient(app)

@pytest.mark.integration
def test_chat_real_respuesta_coherente():
    with TestClient(app) as client:
        response = client.post("/chat/", json={"question": "¿Cómo se prepara un Freshpresso?"})
        assert response.status_code == 200
        data = response.json()
        assert "freshpresso" in data["answer"].lower()
