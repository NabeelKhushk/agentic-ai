import asyncio
import os
from dotenv import load_dotenv, find_dotenv

from agents import Agent, AsyncOpenAI, ModelSettings, OpenAIChatCompletionsModel, RunConfig, Runner, function_tool, set_default_openai_api, set_default_openai_client, set_tracing_disabled

# Load environment variables
load_dotenv(find_dotenv())

# 🚫 Disable tracing for clean output (optional for beginners)
set_tracing_disabled(disabled=True)

set_default_openai_api("chat_completions")


external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(external_client)

agent: Agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant", 
    model="gemini-2.5-flash")


async def main():
    result = await Runner.run(
        agent,
        "Hello",
    )
    print(result.final_output)

asyncio.run(main())
