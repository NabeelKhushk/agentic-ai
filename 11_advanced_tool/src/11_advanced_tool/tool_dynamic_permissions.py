import asyncio
from dataclasses import dataclass
import os
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv, find_dotenv
from agents import Agent, AgentBase, AsyncOpenAI, MaxTurnsExceeded, OpenAIChatCompletionsModel, RunConfig, RunContextWrapper, Runner, StopAtTools, function_tool
from pydantic import BaseModel

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

class UserContext(BaseModel):
    user_id: str
    subscription_tier: str = "free"  # free, premium, enterprise
    has_permission: bool = False

def premium_feature_enabled(context: RunContextWrapper, agent: Agent) -> bool:
    print(f"premium_feature_enabled()")
    print(context.context.subscription_tier, context.context.subscription_tier in ["premium", "enterprise"])
    return context.context.subscription_tier in ["premium", "enterprise"]

@function_tool(is_enabled=premium_feature_enabled)
def get_weather(city: str) -> str:
    print(f"[ADV] get_weather()")
    return "Weather is sunny"


# This agent will use the custom LLM provider
agent = Agent(
    name="Assistant",
    instructions="You only respond in haikus.",
    model=llm_model,
    tools=[get_weather]
)

async def main():
    # context = UserContext(user_id="123", subscription_tier="premium", has_permission=True)
    context = UserContext(user_id="123", subscription_tier="basic", has_permission=True)

    result = await Runner.run(
        agent,
        "Call the get_weather tool with city 'London'",
        context=context,
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
    
