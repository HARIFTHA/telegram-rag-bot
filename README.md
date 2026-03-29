# Telegram Mini-RAG Bot

A lightweight GenAI-powered Telegram bot that answers user queries using a Retrieval-Augmented Generation (RAG) system built on a small knowledge base.

* Features
* Telegram bot interface
*  /ask <query> — Ask questions from knowledge base
* Retrieves relevant context using embeddings
* Generates answers using an LLM
* Fast and lightweight local setup
* Uses small document dataset (Markdown/Text)
* Project Goal

#### This project demonstrates a simple RAG (Retrieval-Augmented Generation) pipeline:
Receive user query via Telegram
Retrieve relevant document chunks
Generate contextual answer using LLM
Send response back to user

### System Architecture:
* User (Telegram)
      ↓
* Telegram Bot (telegram_bot.py)
      ↓
* Retriever (retriever.py)
      ↓
* Embedding Model (embedder.py)
      ↓
* Vector DB (vectors.db)
      ↓
* Context + Query
      ↓
* LLM (Phi-3 via Ollama)
      ↓
* Response → User

### Tech Stack:
* Bot Framework: python-telegram-bot
* Embeddings: sentence-transformers (all-MiniLM-L6-v2)
* Vector DB: SQLite / sqlite-vec
* LLM: Ollama (LLaMA 3 / Mistral / Phi-3) (or OpenAI API)
* Language: Python

### Project Structure:
telegram-rag-bot/
* │── bot/
* │   ├── __init__.py
* │   └── telegram_bot.py
* │
* │── db/
* │   └── vectors.db
* │
* │── docs/
* │   ├── company_policy.md
* │   ├── python_faq.md
* │   └── recipes.md
* │
* │── rag/
* │   ├── chunker.py
* │   ├── embedder.py
* │   ├── retriever.py
* │   └── llm.py
* │
* │── ingest.py
* │── main.py
* │── requirements.txt
* │── .gitignore

### Tech Stack:
* Bot: python-telegram-bot
* Embeddings: sentence-transformers (all-MiniLM-L6-v2)
* Vector DB: SQLite (vectors.db)
* LLM Runtime: Ollama
* Model: Phi-3
* Language: Python

#### How It Works:
1. Step 1: Document Ingestion
Load documents from /docs
Split into chunks
Generate embeddings
Store in SQLite database
2. Step 2: Query Handling
User sends /ask <query>
Query is embedded
Top-K relevant chunks retrieved
3. Step 3: Response Generation
Context + query → prompt
Sent to LLM
Final answer returned to user

### Model Details:
* Embedding Model: all-MiniLM-L6-v2
* LLM: Phi-3 (via Ollama)
* Runs locally → no API cost
* Good balance of speed + quality

### Evaluation Highlights:
✔ Clean modular design
✔ Efficient retrieval pipeline
✔ Local LLM usage (no external dependency)
✔ Fast response time

### 👨‍💻 Author
Hariftha

### Summary:
This project demonstrates a modular RAG pipeline integrated with Telegram using a local LLM (Phi-3 via Ollama), enabling efficient and private question-answering over custom documents.
