import asyncio
import os
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv, find_dotenv
from agents import Agent, AsyncOpenAI, MaxTurnsExceeded, OpenAIChatCompletionsModel, RunConfig, Runner, StopAtTools, function_tool

# 0. Load environment variables
load_dotenv(find_dotenv())

# 1. Define the LLM Provider (Gemini via OpenAI-compatible API)
external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 2. Define the Model
llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

# 3. Configure the Run settings
run_config = RunConfig(
    model=llm_model,
    model_provider=external_client,
    tracing_disabled=True
)

@function_tool
def get_weather(city: str) -> str:
    return f"Sunny"

base_agent: Agent = Agent(name="WeatherAgent", model=llm_model, tools=[get_weather])
print(base_agent.tools)

async def main():
    try:
        res = await Runner.run(base_agent, "What is weather in Lahore", max_turns=2)
        print(res.new_items)
    except MaxTurnsExceeded as e:
        print(f"Max turns exceeded: {e}")

if __name__ == "__main__":
    asyncio.run(main())