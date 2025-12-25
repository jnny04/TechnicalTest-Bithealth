from typing import List
from src.domain.models import Document

class InMemoryStore:
    def __init__(self):
        self.docs = []

    def add(self, document: Document) -> bool:
        self.docs.append({
            'id': document.id,
            'vector': document.vector,
            'text': document.text
        })
        return True
    
    def search(self, vector: List[float], query: str, limit: int = 2) -> List[str]:
        results = [d["text"] for d in self.docs if query.lower() in d["text"].lower()]
        if not results and self.docs:
            results = [self.docs[0]["text"]]
        return results[:limit]

    def get_count(self) -> int:
        return len(self.docs)

    def is_ready(self) -> bool:
        return False 
