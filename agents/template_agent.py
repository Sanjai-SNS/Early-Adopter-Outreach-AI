# agents/template_agent.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.6
)

def create_templates(persona, communities, outreach_style):
    prompt = f"""
You are an expert in cold outreach. Based on the following:
- Persona: {persona}
- Communities: {communities}
- Outreach Insights: {outreach_style}

Generate 3 personalized outreach messages:
1. Email
2. Direct Message (DM)
3. Community Post (e.g., IndieHackers, Reddit)

Format each as:
[Type]
Message: <content>
"""
    response = llm.invoke(prompt)
    return {"templates": response.content.strip()}
