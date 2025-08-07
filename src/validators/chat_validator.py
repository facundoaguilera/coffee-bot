## validators/chat_validators.py
def validate_question(question: str):
    if not question:
        raise ValueError("Por favor, escribe una pregunta sobre café.")
