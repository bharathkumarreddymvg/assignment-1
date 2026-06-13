---

# Persistent Sales Assistant Agent

## 🚀 Overview
This project implements a hosted conversational API for a **Persistent Sales Assistant Agent**.  
The agent remembers context across sessions, uses real tools to answer questions about a product catalog, and produces a self‑evaluation score on every response.

---

## 🧩 Features
- **Persistent Memory** across sessions stored in SQLite (swappable backend).
- **Tool Use**:
  - `search_catalog(query)` → searches product catalog JSON.
  - `get_user_memory(user_id)` → retrieves past facts from DB.
  - `flag_for_human(user_id, reason)` → escalates low‑confidence responses.
- **Self‑Evaluation** block on every response with groundedness, relevance, confidence, and reasoning.
- **API Endpoints**:
  - `POST /chat/{user_id}` → send message, get response + eval.
  - `GET /chat/{user_id}/history` → full conversation history.
  - `DELETE /chat/{user_id}/memory` → wipe memory.
  - `GET /catalog` → product catalog.
  - `GET /health` → service health check.

---

## 📂 Architecture

```
app/
  api/          -> route handlers
  agents/       -> agent loop, tool definitions, eval logic
  memory/       -> memory abstraction (SQLite now, swappable later)
  tools/        -> search_catalog, get_user_memory, flag_for_human
  services/     -> chat service, eval service
  models/       -> Pydantic schemas
  db/           -> SQLAlchemy models, migrations
main.py
catalog.json
```

---

## 🖼️ Architecture Diagram

```
User Message
     |
     v
   API Layer (/chat)
     |
     v
   Agent Loop
     |
     +--> Tools (search_catalog, get_user_memory)
     |
     v
   Eval Service (self-scoring)
     |
     v
 Response JSON (with eval block)
```

---

## 🗄️ Memory Design
- Current: SQLite table storing `(user_id, message, response)`.
- At scale: Replace with Postgres or vector DB (Mem0, Pinecone).
- Abstraction ensures only `memory/store.py` changes.

---

## 📊 Eval Design
- Self‑scoring prompt generates groundedness, relevance, confidence.
- Always structured JSON.
- Limitation: subjective scores; at scale, replace with external eval model.

---

## 🧪 Demo (Cross‑Session Memory)

### Call 1: Set context
```bash
curl -X POST "https://your-railway-url/chat/123" \
  -H "Content-Type: application/json" \
  -d '{"message":"What is your enterprise pricing?"}'
```

### Call 2: Use memory
```bash
curl -X POST "https://your-railway-url/chat/123" \
  -H "Content-Type: application/json" \
  -d '{"message":"Does that include SSO?"}'
```

The second call uses memory from the first call without resending context.

---

## 🌐 Hosting
- Deployed on **Railway**
- Live URL: `https://your-railway-url`

---

## ✅ Evaluation Criteria
- Memory persists across calls.
- Tools are real functions.
- Eval block always present.
- Clean architecture with abstractions.
- README includes diagram, design decisions, curl demo, and live URL.

---

This README gives your repo everything evaluators need: architecture, design decisions, curl demo, and hosting details.  

Would you like me to also add a **Railway deployment guide section** (step‑by‑step c
