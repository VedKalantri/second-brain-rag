# 🧠 Second Brain RAG

A Retrieval-Augmented Generation (RAG) application that transforms your Notion notes into an intelligent personal knowledge assistant.

Instead of searching through pages manually, you can ask questions in natural language, and the system retrieves the most relevant notes using semantic search before generating an answer with Google Gemini.

---

## Features

- Notion API Integration
- Automatic Text Extraction
- Recursive Text Chunking
- Sentence Transformer Embeddings
- ChromaDB Vector Database
- Semantic Search
- Google Gemini Powered Answers
- Source Chunk Display

---

## Architecture

```

```
                    Notion
                       │
                       ▼
              Fetch Notes
                       │
                       ▼
             Extract Plain Text
                       │
                       ▼
                Chunk Notes
                       │
                       ▼
        Sentence Transformers
       (BAAI/bge-small-en-v1.5)
                       │
                       ▼
                 ChromaDB
             (Vector Database)
                       │
             User Question
                       │
                       ▼
             Query Embedding
                       │
                       ▼
           Semantic Retrieval
                       │
                       ▼
             Google Gemini
                       │
                       ▼
               Final Response
```

---

## Tech Stack

- Python
- Notion API
- Sentence Transformers
- ChromaDB
- Google Gemini
- LangChain Text Splitters

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/second-brain-rag.git

cd second-brain-rag
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
NOTION_API_KEY=your_notion_api_key

GEMINI_API_KEY=your_gemini_api_key
```

---

## Index your Notes

Fetch notes from Notion

```bash
python fetch_notion.py
```

Generate embeddings and store them in ChromaDB

```bash
python store_embeddings.py
```

---

## Start the RAG Chatbot

```bash
python rag.py
```

---

## Example

**Question**

```
What are Docker Volumes?
```

**Answer**

```
Volumes are used to store persistent data outside containers.
Even if a container is deleted, the data remains available.
```

---

## Current Limitations (Version 1)

- Supports a single Notion page
- Manual synchronization
- Full database rebuild required after updates
- Terminal-based interface

---

## Planned Features (Version 2)

- Automatic Notion synchronization
- Multi-page & workspace support
- Incremental indexing
- Rich metadata
- Better retrieval pipeline
- Streamlit / React UI
- Conversation history
- Source citations
- Docker deployment
- Cloud deployment
- Authentication
- Production-ready architecture

---

## Project Status

✅ Version 1 Completed

🚀 Version 2 In Development
