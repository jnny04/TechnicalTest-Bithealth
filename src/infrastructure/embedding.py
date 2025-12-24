import hashlib
import random
from typing import List

class FakeEmbeddingService:
    def embed(self, text: str) -> List[float]:
        hash_seed = int(hashlib.sha256(text.encode()).hexdigest(), 16) % 10**8
        random.seed(hash_seed)
        return [random.random() for _ in range(128)]