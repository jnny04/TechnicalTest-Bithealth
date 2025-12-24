from typing import List, Dict, Any

class InMemoryStore:
    def __init__(self):
        self.docs: List[Dict[str, Any]] = []

    def add(self, doc_id: int, vector: List[float], text: str) -> bool:
        self.docs.append({
            "id": doc_id,
            "vector": vector,
            "text": text
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