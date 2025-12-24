import time
from fastapi import APIRouter, HTTPException
from src.core.logger import logger
from src.domain.schemas import (
    QuestionRequest, QuestionResponse, 
    DocumentRequest, DocumentResponse, 
    StatusResponse
)

def create_router(engine, storage):
    router = APIRouter()

    @router.post(
        "/ask", 
        response_model=QuestionResponse,
        summary="Execute RAG workflow"
    )
    def ask(req: QuestionRequest):
        try:
            start_time = time.time()            
            res = engine.run(req.question)
            
            duration = round(time.time() - start_time, 3)
            
            return {
                "question": req.question,
                "answer": res["answer"],
                "context_used": res.get("context", []),
                "latency_sec": duration
            }
        except Exception as e:
            logger.error(f"RAG workflow failure at /ask endpoint: {e}")
            raise HTTPException(status_code=500, detail="Internal AI engine error occurred.")

    @router.post(
        "/add", 
        response_model=DocumentResponse,
        summary="Add new document"
    )
    def add(req: DocumentRequest):
        try:
            doc_id = engine.add_document(req.text)
            return {"id": doc_id, "status": "added"}
        except Exception as e:
            logger.error(f"Document storage failure at /add endpoint: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    @router.get(
        "/status", 
        response_model=StatusResponse,
        summary="Get system status"
    )
    def status():
        return {
            "qdrant_ready": storage.is_ready(),
            "in_memory_docs_count": storage.get_count(),
            "graph_ready": True
        }

    return router