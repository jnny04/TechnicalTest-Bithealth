# TechnicalTest-Bithealth
My submission for the BitHealth Associate AI Engineer Take Home Assessment. A clean and modular refactor of a RAG service using FastAPI and LangGraph

## RAG Service Refactor
The original code was a working but pretty messy one-file script. I’ve completely refactored it into a modular, clean, and organized system that’s actually ready for a production environment.

## What I Improved
I didn't just move files around. I fundamentally changed how the app is put together to make it more reliable and easier to scale.
- I moved away from the "all-in-one" script and used a **Layered Architecture**. This separates the API from the business logic and the database.
- I kept the **LangGraph** requirement but moved the workflow into a dedicated engine class. This keeps the RAG steps easy to follow.
- The app can still fall back to in-memory storage, but I made the **Qdrant** part smarter. It now checks if a collection exists instead of wiping your data every time you restart.
- By using **Protocols**, I made the app agnostic. You can swap the database or embedding tool without breaking the whole thing.
- I used a more stable hashing method for the fake embeddings so that the same text always gives you the same vector.

## Project Structure
- src/api/: All the FastAPI stuff (routes and endpoints).
- src/core/: Boring but important stuff like config and logging.
- src/domain/: The "brains" — schemas and the rules (interfaces) for the app.
- src/infrastructure/: The actual tools, like the Qdrant client and embedding service.
- src/services/: The RAG Engine that runs the LangGraph workflow.

## Getting Started
If you want to run this locally, it's pretty straightforward:
1. Install the goods: pip install -r requirements.txt
2. Fire it up: uvicorn main:app --reload
3. Check the docs: Head over to http://localhost:8000/docs to play with the /ask and /add endpoints.

## Thinking Process
I wrote a separate **notes.md** file that explains my design choices, the trade-offs I made, and why I built it this way. Definitely give that a read if you want to see how I think about code quality!
