from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from src.core.config import settings
from src.core.logger import logger

class QdrantStore:
    def __init__(self):
        self.client = QdrantClient(settings.QDRANT_URL)
        self.collection = settings.COLLECTION_NAME
        self._init_collection()

    def _init_collection(self):
        # PERBAIKAN: Cek eksistensi koleksi agar data tidak hilang (Persistence)
        try:
            collections = self.client.get_collections().collections
            exists = any(c.name == self.collection for c in collections)
            
            if not exists:
                self.client.create_collection(
                    collection_name=self.collection,
                    vectors_config=VectorParams(size=settings.VECTOR_SIZE, distance=Distance.COSINE)
                )
                logger.info(f"Collection {self.collection} created.")
            else:
                logger.info(f"Collection {self.collection} already exists. Skipping creation.")
        except Exception as e:
            logger.error(f"Failed to initialize Qdrant: {e}")
            raise e