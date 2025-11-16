import asyncio
import os
from dotenv import load_dotenv, find_dotenv

from agents import Agent, AsyncOpenAI, ModelSettings, OpenAIChatCompletionsModel, RunConfig, Runner, function_tool, set_tracing_disabled

# Load environment variables
load_dotenv(find_dotenv())

# 🚫 Disable tracing for clean output (optional for beginners)
set_tracing_disabled(disabled=True)

external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

run_config = RunConfig(
    model=llm_model,
    model_provider=external_client,
)


agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
    )

async def main():
    result = await Runner.run(
        agent,
        "Tell me about recursion in programming.",
        run_config=run_config
    )
    print(result.final_output)

asyncio.run(main())
