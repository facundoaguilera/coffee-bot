## context/rag_engine.py
from pypdf import PdfReader
from src.context.interfaces import IContextRetriever
def load_pdf_chunks(path: str, chunk_size: int = 200) -> list[str]:
    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"
        
    text = text.replace('\xa0', ' ').strip()
    words = text.split()
    
    chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    
    return chunks

def build_index(path: str, vectorizer: IContextRetriever):
    chunks = load_pdf_chunks(path)
    vectorizer.fit(chunks)
    return vectorizer

