import asyncio
from dataclasses import dataclass
import os
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv, find_dotenv
from agents import Agent, AgentBase, AsyncOpenAI, MaxTurnsExceeded, OpenAIChatCompletionsModel, RunConfig, RunContextWrapper, Runner, StopAtTools, function_tool

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

@function_tool(description_override="", failure_error_function="")
def get_weather(city: str) -> str:
    try:
        # If Call Fails Call another service i.e get_weather_alternative
        ...
    except ValueError:
        raise ValueError("Weather service is currently unavailable.")
    except TimeoutError:
        raise TimeoutError("Weather service request timed out.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")

base_agent: Agent = Agent(name="WeatherAgent", instructions="", model=llm_model, tools=[get_weather])

async def main():
    res = await Runner.run(base_agent, "What is weather in Lahore")
    print(res.final_output)

if __name__ == "__main__":
    asyncio.run(main())