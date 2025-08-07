## context/vector_context.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from context.interfaces import IContextRetriever

class VectorContextRetriever(IContextRetriever):
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.chunk_vectors = None
        self.pdf_chunks = []

    def fit(self, chunks: list[str]) -> None:
        self.pdf_chunks = chunks
        self.chunk_vectors = self.vectorizer.fit_transform(chunks)

    def get_context(self, query: str, top_k: int = 3) -> tuple[str, float]:
        query_vec = self.vectorizer.transform([query])
        similarity = cosine_similarity(query_vec, self.chunk_vectors)
        top_indices = similarity[0].argsort()[-top_k:][::-1]
        top_chunks = [self.pdf_chunks[i] for i in top_indices]
        top_score = similarity[0][top_indices[0]]
        return "\n".join(top_chunks), top_score