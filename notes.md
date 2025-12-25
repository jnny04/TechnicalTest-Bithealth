# Implementation Notes - RAG Service Refactor

## Main Design Decisions
I restructured the application using a Layered Architecture to ensure a clear Separation of Concerns. While this might seem extensive for a demo, I prioritized a "production-ready" mindset as requested. By isolating Infrastructure from Business Logic, the system becomes much more maintainable. I also introduced a Document dataclass to encapsulate related data (text, vector, and ID) into a single validated object, moving away from the unstructured dictionaries used in the original version.

## Trade-offs Considered
I considered using simple classes or Abstract Base Classes (ABC) for the interfaces but ultimately chose Protocols. The trade-off is a bit more abstraction, but it rewards us with a more "Pythonic" and flexible structure (Structural Typing). This makes mocking during testing much simpler without forcing a rigid inheritance hierarchy on every new storage implementation.

## Maintainability Improvements
The code is much easier to manage now because I got rid of all those global variables that can cause headaches later. By using Dependency Injection, we can now test each part of the app on its own. I also made the QdrantStore a bit smarter it now checks if a collection already exists instead of just wiping it and starting over every time the app runs. This ensures our data actually stays persistent, making the whole system more reliable and ready to grow.
