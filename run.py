from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Search for Cursor code editor, download it for Windows",
        llm=ChatOllama(
            model="qwen2.5:7b",
            num_ctx=32000,
        ),
    )
    await agent.run()

asyncio.run(main())