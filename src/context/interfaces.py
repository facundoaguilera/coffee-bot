## context/interfaces.py
from abc import ABC, abstractmethod

class IContextRetriever(ABC):
    @abstractmethod
    def fit(self, chunks: list[str]) -> None:
        pass

    @abstractmethod
    def get_context(self, question: str, top_k: int = 1) -> tuple[str, float]:
        pass