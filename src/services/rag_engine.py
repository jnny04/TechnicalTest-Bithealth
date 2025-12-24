import uuid
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from src.domain.interfaces import DocumentStore, EmbeddingService

class GraphState(TypedDict):
    question: str
    context: List[str]
    answer: str

class RagEngine:
    def __init__(self, storage: DocumentStore, embedder: EmbeddingService):
        self.storage = storage
        self.embedder = embedder
        self.workflow = self._build_graph()

    # Build the graph structure for RAG
    def _build_graph(self):
        builder = StateGraph(GraphState)
        
        builder.add_node("retrieve", self._retrieve_node)
        builder.add_node("answer", self._answer_node)
        
        builder.set_entry_point("retrieve")
        builder.add_edge("retrieve", "answer")
        builder.add_edge("answer", END)
        
        return builder.compile()

    # Retrieve context based on the question
    def _retrieve_node(self, state: GraphState) -> dict:
        emb = self.embedder.embed(state["question"])
        context = self.storage.search(emb, state["question"])
        return {"context": context}

    # Generate answer based on retrieved context matching main.py logic
    def _answer_node(self, state: GraphState) -> dict:
        ctx = state["context"]
        if not ctx:
            return {"answer": "Sorry, I don't know."}
        
        answer = f"I found this: '{ctx[0][:100]}...'"
        return {"answer": answer}

    # Coordinate embedding process and document storage
    def add_document(self, text: str) -> int:
        doc_id = uuid.uuid4().int >> 96
        vector = self.embedder.embed(text)
        self.storage.add(doc_id, vector, text)
        return doc_id

    # Execute the RAG workflow
    def run(self, question: str):
        return self.workflow.invoke({"question": question})