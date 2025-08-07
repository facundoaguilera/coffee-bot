import pytest
from unittest.mock import MagicMock
from src.services.chat_service import ChatService
from src.context.vector_context import VectorContextRetriever

@pytest.mark.unit
def test_chat_service_responde_con_contexto_y_respuesta_simulada():
    # 1. Crear un VectorContextRetriever real y entrenarlo con datos simulados
    chunks = [
        "El espresso se prepara con agua caliente a presión.",
        "El café filtrado usa una proporción de 1:15 de café a agua.",
        "La temperatura ideal del agua es entre 90 y 96 grados Celsius."
    ]
    retriever = VectorContextRetriever()
    retriever.fit(chunks)

    # 2. Crear un generador simulado (mock de Gemini)
    mock_generator = MagicMock()
    mock_generator.generate.return_value = "Para preparar espresso, usá agua a presión."

    # 3. Instanciar el servicio con dependencias reales + mock
    service = ChatService(retriever, mock_generator)

    # 4. Ejecutar el método ask
    question = "¿Cómo se hace un espresso?"
    answer   = service.handle_chat(question)

    # 5. Aserciones
    assert "espresso" in answer.lower()
    assert "agua caliente" in answer.lower() or "espresso" in answer.lower()
    
@pytest.mark.unit
def test_chat_service_pregunta_vacia():
    
    retriever = MagicMock()
    generator = MagicMock()
    service = ChatService(retriever, generator)
    answer = service.handle_chat("")

    assert "escribe una pregunta sobre café" in answer.lower()

@pytest.mark.unit
def test_chat_service_pregunta_fuera_de_contexto():
    retriever = MagicMock()
    retriever.get_context.return_value = ("contexto simulado", 0.05)
    generator = MagicMock()
    service = ChatService(retriever, generator)
    answer = service.handle_chat("¿como estas hoy?")

    assert "No estoy preparado para responder esa pregunta,"
    " por favor pregunta algo relacionado a Café." == answer

@pytest.mark.unit
def test_chat_service_error_interno_general():
    retriever = MagicMock()
    retriever.get_context.return_value = ("contexto simulado", 0.9)
    generator = MagicMock()
    generator.generate.side_effect = Exception("Falla simulada en Gemini")
    service = ChatService(retriever, generator)
    answer = service.handle_chat("¿Qué es el café espresso?")

    assert "hubo un error" in answer.lower()