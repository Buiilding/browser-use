from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Go to deadhouse.org and give me the first caption",
        llm=ChatGoogleGenerativeAI(model = "gemini-1.5-flash", ),
    )
    await agent.run()

asyncio.run(main())