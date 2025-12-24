# Implementation Notes - RAG Service Refactor

## Main Design Decisions
I restructured everything using a Layered Architecture to make sure there's a clear separation of concerns. I realize this might feel a bit broad or "heavy" for just a small demo, but I wanted to show how the app could actually grow into a production-scale system. By keeping the Infrastructure separate from the Business Logic, the team can easily swap out things like the Embedding provider or the Vector Database in the future without having to tear the whole app apart. I also moved the core RAG logic into the RagEngine and used Protocols to keep the API routes thin and the code decoupled.

## Trade-offs Considered
I spent some time thinking about how to handle the interfaces and ended up choosing Protocols. I went this route because it’s a lot more flexible and feels more "Pythonic." It makes it much easier to swap things out or mock them for testing without being forced into a rigid class structure. While it might seem a bit extra for a small app, it keeps the components decoupled from the start.

## Maintainability Improvements
The code is much easier to manage now because I got rid of all those global variables that can cause headaches later. By using Dependency Injection, we can now test each part of the app on its own. I also made the QdrantStore a bit smarter it now checks if a collection already exists instead of just wiping it and starting over every time the app runs. This ensures our data actually stays persistent, making the whole system more reliable and ready to grow.