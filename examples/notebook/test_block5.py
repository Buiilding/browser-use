# run_agent.py
import sys
import asyncio
import nest_asyncio

# Apply nest_asyncio (still useful for nested event loops)
nest_asyncio.apply()

# Switch event loop policy for Windows
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from langchain_ollama import ChatOllama
from browser_use import Agent, Browser, BrowserConfig

llm = ChatOllama(
    model="qwen2.5:7b",
    num_ctx=32000,
)

config = BrowserConfig(
    headless=True,
    # disable_security=True
)

browser = Browser(config=config)

async def main():
    agent = Agent(
        task="What is Langgraph",
        llm=llm,
        browser=browser,
        generate_gif=False
    )
    result = await agent.run()

    for action in result.action_results():
        print(action.extracted_content, end="\r", flush=True)
        print("\n\n")

    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
