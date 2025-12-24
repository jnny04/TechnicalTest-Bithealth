import os

class Settings:
    APP_TITLE: str = "Learning RAG Demo - BitHealth Refactor"
    QDRANT_URL: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    COLLECTION_NAME: str = "demo_collection"
    VECTOR_SIZE: int = 128

settings = Settings()