# SHL Assessment Recommendation Agent

An AI-powered assessment recommendation system built for the SHL Assessment Recommendation challenge.

The application recommends the most relevant SHL assessments based on natural language hiring requirements using Large Language Models (LLMs), semantic search, and vector similarity search.

---

# Features

- AI-powered intent detection using Mistral LLM
- Natural language hiring query understanding
- Semantic search using HuggingFace Embeddings
- FAISS vector search for fast retrieval
- SHL catalog search across 377 assessments
- FastAPI REST API
- Swagger API documentation
- Modular architecture
- Production-ready project structure

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.10+ | Backend |
| FastAPI | REST API |
| LangChain | LLM Framework |
| Mistral AI | Intent Analysis & Response Generation |
| HuggingFace BGE Small | Embeddings |
| Sentence Transformers | Embedding Generation |
| FAISS | Vector Database |
| NumPy | Vector Processing |
| Pydantic | Data Validation |

---

# Project Architecture

```
User Query
      │
      ▼
LLM (Mistral)
Intent Analysis
      │
      ▼
Search Query Builder
      │
      ▼
HuggingFace Embeddings
      │
      ▼
FAISS Semantic Search
      │
      ▼
Relevant SHL Assessments
      │
      ▼
LLM Response Generation
      │
      ▼
Final Recommendation
```

---

# Project Structure

```
shl-assessment-agent/

│
├── app/
│   ├── api/
│   ├── conversation/
│   ├── core/
│   ├── data/
│   ├── embeddings/
│   ├── llm/
│   ├── models/
│   ├── recommendation/
│   ├── retrieval/
│   ├── services/
│   └── main.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── .env.example
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/minatoNamikage-cyber/shl-assessment-agent.git

cd shl-assessment-agent
```

Create Virtual Environment

```bash
python -m venv shlenv
```

Activate

Windows

```bash
shlenv\Scripts\activate
```

Linux / Mac

```bash
source shlenv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```
MISTRAL_API_KEY=your_api_key

MODEL_NAME=mistral-small-latest

APP_NAME=SHL Assessment Agent

DEBUG=True
```

---

# Build Embeddings

```bash
python -m app.embeddings.index_builder
```

This generates

```
app/data/embeddings.npy
```

---

# Build FAISS Index

```bash
python -m app.retrieval.faiss_index
```

This generates

```
app/data/faiss.index

app/data/metadata.pkl
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# Example API

## Chat

POST

```
/chat
```

Request

```json
{
    "query":"We need a Java Developer for hiring."
}
```

Response

```json
{
  "analysis": {
    "intent":"recommend",
    "role":"Java Developer",
    "purpose":"Hiring"
  },
  "recommendations":[
    ...
  ],
  "response":"Recommended SHL assessments..."
}
```

---

# Search Flow

```
User Query

↓

Intent Detection

↓

Search Query Generation

↓

Embedding Generation

↓

FAISS Search

↓

Top Assessments

↓

Natural Language Response
```

---

# Current Capabilities

- Intent Detection
- Hiring Requirement Analysis
- Semantic Search
- SHL Assessment Recommendation
- Natural Language Responses
- REST API
- Swagger Documentation

---

# Future Improvements

- Hybrid Retrieval (BM25 + FAISS)
- Conversation Memory
- Multi-turn Conversation Support
- Cross Encoder Re-ranking
- Evaluation Dashboard
- Frontend Interface
- Docker Support
- CI/CD Pipeline

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Application Status |
| GET | /health | Health Check |
| POST | /chat | Assessment Recommendation |
| GET | /docs | Swagger Documentation |

---

# Author

**Siddharth Kumar**

B.Tech Information Technology

Artificial Intelligence & Machine Learning Enthusiast

GitHub

https://github.com/minatoNamikage-cyber

---

# License

This project was developed for the SHL Assessment Recommendation Challenge.

For educational and evaluation purposes only.
