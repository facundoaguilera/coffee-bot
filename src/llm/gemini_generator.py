## llm/gemini_generator.py
from src.llm.interfaces import IResponseGenerator
from google import genai
from google.genai import types
import os

class GeminiGenerator(IResponseGenerator):
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("La API Key de Gemini no está configurada.")
        self.client = genai.Client()

    def generate(self, context: str, question: str) -> str:
        contents = [
            types.Content(
                parts=[
                    types.Part(
                        text=(
                            "Responde solamente en español. "
                            "Si la pregunta está en otro idioma que no sea español, responde: "
                            "\"Lo siento, solo puedo responder preguntas en español.\"\n\n"
                            "Si la pregunta no está relacionada al café, responde: "
                            "\"Lo siento, solo puedo responder preguntas sobre café.\"\n\n"
                            f"Contexto:\n{context}\n\n"
                            f"Pregunta:\n{question}"
                        )
                    )
                ]
            )
        ]

        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=contents,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(thinking_budget=0)
                )
            )
            return response.text

        except Exception as e:
            print("Error con Gemini SDK:", e)
            return "Hubo un error al generar la respuesta."