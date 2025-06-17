# agents/persona_agent.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

def identify_persona(description: str):
    prompt = f"You are a startup marketing expert. Based on the startup idea: '{description}', identify the ideal early adopter persona and suggest digital communities (e.g., Reddit, IndieHackers, Discord) they hang out in."
    response = llm.invoke(prompt)
    if "Communities:" in response.content:
        persona, communities = response.content.split("Communities:")
        return persona.strip(), [c.strip() for c in communities.split(",")]
    return response.content.strip(), []
