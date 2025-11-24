import os
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv, find_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner, StopAtTools, function_tool

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
    """A simple function to get the weather for a user."""
    return f"Sunny"

@function_tool
def get_travel_plan(city: str) -> str:
    """Plan Travel for your city"""
    return f"Travel Plan is not available"

base_agent: Agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful assistant.",
    model=llm_model,
    tools=[get_weather, get_travel_plan],
    tool_use_behavior=StopAtTools(stop_at_tool_names=["get_travel_plan"])
)

res = Runner.run_sync(base_agent, "What is weather in Lahore")
res = Runner.run_sync(base_agent, "Make me travel plan for Lahore")
print(res.final_output)

# 1. NLP answer = loop finished
# 2. tool call = loop continue - loop finish

# tool call = ASK Question from Human = loop pause