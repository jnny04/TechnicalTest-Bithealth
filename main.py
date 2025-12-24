from fastapi import FastAPI
from src.core.config import settings
from src.core.logger import logger
from src.infrastructure.storage.qdrant_store import QdrantStore
from src.infrastructure.storage.memory_store import InMemoryStore
from src.infrastructure.embedding import FakeEmbeddingService
from src.services.rag_engine import RagEngine
from src.api.routes import create_router

def create_app():
    app = FastAPI(title=settings.APP_TITLE)

    # 1. Initialize Infrastructure
    embedder = FakeEmbeddingService()
    try:
        storage = QdrantStore()
        logger.info("Connected to Qdrant Storage")
    except Exception:
        storage = InMemoryStore()
        logger.warning("Qdrant unavailable, using In-Memory fallback")

    # 2. Initialize Business Logic
    engine = RagEngine(storage, embedder)

    # 3. Mount Routes
    router = create_router(engine, storage)
    app.include_router(router)

    return app

app = create_app()