from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Create a Json format for a list of Machine Learning Jobs in the US, including the job title, company name, location, and salary. There is no need to relate to my current location",
        llm=ChatGoogleGenerativeAI(model = "gemini-2.0-flash"),
        max_failures=5
    )
    await agent.run()

asyncio.run(main())