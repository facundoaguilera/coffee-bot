import pytest
from unittest.mock import MagicMock
from src.llm.gemini_generator import GeminiGenerator

@pytest.mark.unit
def test_generate_response_exitoso(monkeypatch):
    # Setear variable de entorno
    monkeypatch.setenv("GEMINI_API_KEY", "fake-key")

    # Instanciar y mockear el cliente
    generator = GeminiGenerator()
    mock_response = MagicMock()
    mock_response.text = "Respuesta simulada"
    generator.client.models.generate_content = MagicMock(return_value=mock_response)

    result = generator.generate("contexto", "¿Qué es un espresso?")
    assert result == "Respuesta simulada"


@pytest.mark.unit
def test_generate_response_falla(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "fake-key")

    generator = GeminiGenerator()
    generator.client.models.generate_content = MagicMock(side_effect=Exception("Error simulado"))

    result = generator.generate("contexto", "¿Qué es un espresso?")
    assert "Hubo un error" in result
    
@pytest.mark.unit
def test_gemini_generator_sin_api_key(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    with pytest.raises(ValueError, match="La API Key de Gemini no está configurada."):
        GeminiGenerator()