## llm/interfaces.py
from abc import ABC, abstractmethod

class IResponseGenerator(ABC):
    @abstractmethod
    def generate(self, context: str, question: str) -> str:
        pass
