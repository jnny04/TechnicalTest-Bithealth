# Implementation Notes - RAG Service Refactor

## Main Design Decisions
I restructured the application using a Layered Architecture to enforce a clear separation of concerns. By introducing a `domain` layer with `Protocol` interfaces, I implemented the Dependency Inversion Principle, ensuring that the `RagEngine` remains agnostic of the specific storage or embedding implementation. Key business logic, such as coordinating embeddings and document storage, was encapsulated within the `RagEngine` to keep the API routes thin and focused solely on HTTP handling.

## Trade-offs Considered
One significant trade-off was the choice between using **Abstract Base Classes (Inheritance)** versus **Protocols (Structural Subtyping)** for the service interfaces. I chose **Protocols** because they offer greater flexibility in Python's dynamic ecosystem, allowing for easier mocking during unit testing and supporting "duck typing" without forcing a rigid class hierarchy. While ABCs provide more explicit enforcement, Protocols better support the decoupled nature of this modular design.

## Maintainability Improvements
This version significantly improves maintainability through decoupling and enhanced robustness. By removing global states and utilizing Dependency Injection, components can now be tested in isolation. Additionally, I improved the `QdrantStore` implementation to verify collection existence instead of recreating it on every start, ensuring data persistence. The organized folder structure ensures that infrastructure changes (like upgrading the vector database) do not leak into the business logic or API layers, making the codebase scalable for future production needs.