# agents/engagement_agent.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5
)

def recommend_engagement_strategy(description: str):
    prompt = f"""
You're an expert in startup user acquisition. Based on this startup idea: '{description}', recommend:

1. Best time of day & week to send outreach
2. Follow-up cadence (how many times, how often)
3. Tips to collect feedback & improve response rate
"""
    response = llm.invoke(prompt)
    return response.content.strip()
