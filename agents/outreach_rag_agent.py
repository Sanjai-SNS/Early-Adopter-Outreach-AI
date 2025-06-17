# agents/outreach_rag_agent.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from chains.rag_chain import run_rag_chain

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5
)

def generate_outreach_insights(description: str):
    query = f"What outreach tone and format works best for: {description}?"
    insights = run_rag_chain(query)
    return insights
