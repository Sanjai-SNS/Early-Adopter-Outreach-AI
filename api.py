# 📦 API Server Wrapper for LangChain Agents

from fastapi import FastAPI
from pydantic import BaseModel
from agents.persona_agent import identify_persona
from agents.outreach_rag_agent import generate_outreach_insights
from agents.template_agent import create_templates
from agents.engagement_agent import recommend_engagement_strategy
import os
from dotenv import load_dotenv

# Load environment variables from .env file in the root directory
# Ensure your .env file contains: GOOGLE_API_KEY=your_gemini_api_key
load_dotenv()

app = FastAPI(
    title="Early Adopter Outreach Strategist API",
    description="Agentic API to support early user acquisition strategy for startups",
    version="1.0.0"
)

class StartupInput(BaseModel):
    name: str
    description: str

@app.post("/persona")
def get_persona(data: StartupInput):
    persona, communities = identify_persona(data.description)
    return {
        "persona": persona,
        "communities": communities
    }

@app.post("/outreach")
def get_outreach_insights(data: StartupInput):
    insights = generate_outreach_insights(data.description)
    return {"insights": insights}

@app.post("/templates")
def get_templates(data: StartupInput):
    persona, communities = identify_persona(data.description)
    insights = generate_outreach_insights(data.description)
    templates = create_templates(persona, communities, insights)
    return templates

@app.post("/engagement")
def get_engagement_strategy(data: StartupInput):
    strategy = recommend_engagement_strategy(data.description)
    return {"strategy": strategy}

@app.post("/full")
def full_pipeline(data: StartupInput):
    persona, communities = identify_persona(data.description)
    insights = generate_outreach_insights(data.description)
    templates = create_templates(persona, communities, insights)
    strategy = recommend_engagement_strategy(data.description)
    return {
        "persona": persona,
        "communities": communities,
        "templates": templates,
        "engagement_strategy": strategy
    }

# 🔧 Run the server using:
# uvicorn api:app --reload

# 🧪 Example curl test:
# curl -X POST http://localhost:8000/full \
# -H "Content-Type: application/json" \
# -d '{"name": "TestStartup", "description": "An AI tool for managing remote teams"}'
