import pytest
from unittest.mock import MagicMock
from src.services.rag_engine import RagEngine

def test_rag_engine_flow():
    mock_storage = MagicMock()
    mock_embedder = MagicMock()
    
    mock_storage.search.return_value = ["This is a reference text"]
    mock_embedder.embed.return_value = [0.1] * 128
    
    engine = RagEngine(storage=mock_storage, embedder=mock_embedder)

    result = engine.run("What is AI?")
    
    assert "answer" in result
    assert result["answer"].startswith("I found this:")    
    assert "This is a reference text" in result["answer"]
    
    assert mock_storage.search.called