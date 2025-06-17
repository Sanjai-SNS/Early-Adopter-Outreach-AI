# 🚀 Early Adopter Outreach Strategist

AI-driven strategist for early-stage startups to craft high-conversion outreach strategies using a 4-agent Agentic AI system with LangChain, Gemini (Google Generative AI), and external RAG search.

---

## 🧠 Problem Statement

> First users are hard to find, and cold outreach often fails without personalization.

This app solves that by generating:

* 🎯 Ideal customer personas & where they hang out
* ✉️ Personalized outreach templates (email, DMs, community posts)
* 📚 Style & tone recommendations (via RAG on YC/growth content)
* ⏱️ Outreach timing, follow-ups & engagement tactics

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit *(optional if you add UI)*
* **API Backend**: FastAPI
* **LLM**: Gemini 1.5 via `langchain-google-genai`
* **RAG**: External Web Search (DuckDuckGo)
* **Agents**: LangChain multi-agent pattern
* **Python Version**: `3.12.10`

---

## 📦 Installation

1. **Clone the Repo**

```bash
git clone https://github.com/your-username/early-adopter-strategist.git
cd early-adopter-strategist
```

2. **Create a Virtual Environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install Requirements**

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_actual_gemini_api_key
```

> 💡 You can get the Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

---

## 🚀 Run the API Server

```bash
uvicorn api:app --reload
```

---

## 📬 API Endpoints

All requests accept a JSON payload:

```json
{
  "name": "Your Startup",
  "description": "What your startup does"
}
```

### 1. 🎯 Get Persona + Communities

```bash
curl -X POST http://localhost:8000/persona \
-H "Content-Type: application/json" \
-d '{"name": "YourStartup", "description": "We help creators monetize faster."}'
```

---

### 2. 📚 Outreach Style Insights (RAG)

```bash
curl -X POST http://localhost:8000/outreach \
-H "Content-Type: application/json" \
-d '{"name": "YourStartup", "description": "We help creators monetize faster."}'
```

---

### 3. ✉️ Outreach Templates

```bash
curl -X POST http://localhost:8000/templates \
-H "Content-Type: application/json" \
-d '{"name": "YourStartup", "description": "We help creators monetize faster."}'
```

---

### 4. 📈 Engagement Strategy

```bash
curl -X POST http://localhost:8000/engagement \
-H "Content-Type: application/json" \
-d '{"name": "YourStartup", "description": "We help creators monetize faster."}'
```

---

### 5. 🔁 Full Pipeline

```bash
curl -X POST http://localhost:8000/full \
-H "Content-Type: application/json" \
-d '{"name": "YourStartup", "description": "We help creators monetize faster."}'
```

---

## 📂 Folder Structure

```
early-adopter-strategist/
├── api.py                  # FastAPI server
├── .env                    # Secret keys (excluded from Git)
├── requirements.txt
├── README.md
├── agents/
│   ├── persona_agent.py
│   ├── outreach_rag_agent.py
│   ├── template_agent.py
│   └── engagement_agent.py
├── chains/
│   ├── rag_chain.py
│   └── utils.py
```

---

## 🙌 Contributing

PRs and feedback welcome. This project is MIT licensed.

---

## 📜 License

MIT License. Free for personal and commercial use.
