from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from src.core.config import settings
from src.core.logger import logger
from src.domain.models import Document
from typing import List

class QdrantStore:
    def __init__(self):
        self.client = QdrantClient(settings.QDRANT_URL) 
        self.collection = settings.COLLECTION_NAME 
        self._init_collection() 

    def _init_collection(self):
        try:
            collections = self.client.get_collections().collections
            exists = any(c.name == self.collection for c in collections)
            
            if not exists:
                self.client.create_collection(
                    collection_name=self.collection,
                    vectors_config=VectorParams(
                        size=settings.VECTOR_SIZE, 
                        distance=Distance.COSINE
                    )
                ) 
                logger.info(f"Collection {self.collection} created.") 
            else:
                logger.info(f"Collection {self.collection} already exists. Skipping creation.") 
        except Exception as e:
            logger.error(f"Failed to initialize Qdrant: {e}") 
            raise e
        
    def add(self, document: Document) -> bool:
        try:
            self.client.upsert(
                collection_name=self.collection,
                points=[
                    PointStruct(
                        id=document.id, 
                        vector=document.vector, 
                        payload={'text': document.text, **document.metadata}
                    )
                ]
            )
            return True
        except Exception as e:
            logger.error(f'Failed to add document to Qdrant: {e}')
            return False

    def search(self, vector: List[float], query: str, limit: int = 2) -> List[str]:
        try:
            hits = self.client.search(
                collection_name=self.collection,
                query_vector=vector,
                limit=limit
            )
            return [hit.payload["text"] for hit in hits]
        except Exception as e:
            logger.error(f"Search failed in Qdrant: {e}")
            return []

    def get_count(self) -> int:
        try:
            collection_info = self.client.get_collection(self.collection)
            return collection_info.points_count
        except Exception:
            return 0

    def is_ready(self) -> bool:
        return True
