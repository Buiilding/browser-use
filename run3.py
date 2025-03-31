from langchain_ollama import ChatOllama
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="look for a hiring of an AI engineer from a startup company",
        llm=ChatOllama(model="qwen2.5:7b")
    )
    await agent.run()

asyncio.run(main())