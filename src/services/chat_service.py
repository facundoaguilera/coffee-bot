## services/chat_service.py
from context.interfaces import IContextRetriever
from src.llm.interfaces import IResponseGenerator
from src.validators.chat_validator import validate_question

class ChatService:
    def __init__(self, context_retriever: IContextRetriever, generator: IResponseGenerator):
        self.context_retriever = context_retriever
        self.generator = generator

    def handle_chat(self, question: str) -> str:
        try:
            validate_question(question)
            context, score = self.context_retriever.get_context(question)
            print(f"Score : {score}")
            if score < 0.05:
                return "No estoy preparado para responder esa pregunta, por favor pregunta algo relacionado a Café."
            return self.generator.generate(context, question)
        except ValueError as ve:
            return str(ve)
        except Exception as e:
            print("Error interno:", e)
            return "Hubo un error al generar la respuesta. Intenta más tarde"
