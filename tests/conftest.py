import os
from dotenv import load_dotenv

def pytest_configure():
    load_dotenv()  # Carga variables desde .env automáticamente
    assert os.getenv("GEMINI_API_KEY"), "No se encontró GEMINI_API_KEY en el entorno"