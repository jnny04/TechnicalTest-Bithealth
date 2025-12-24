from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_status_endpoint():
    response = client.get("/status")
    assert response.status_code == 200
    assert "qdrant_ready" in response.json()

def test_add_document():
    payload = {"text": "Learning Python is fun"}
    response = client.post("/add", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "added"

def test_ask_question():
    payload = {"question": "Python"}
    response = client.post("/ask", json=payload)
    assert response.status_code == 200
    assert "I found this:" in response.json()["answer"]