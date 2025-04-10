from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="look for a hiring of an AI engineer from a startup company",
        llm=ChatGoogleGenerativeAI(model = "gemini-2.0-flash"),
    )
    await agent.run()

asyncio.run(main())