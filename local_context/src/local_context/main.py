import asyncio
from dataclasses import dataclass
import os
from dotenv import load_dotenv, find_dotenv

from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, RunContextWrapper, Runner, function_tool

# 0. Load environment variables
load_dotenv(find_dotenv())

# Define a simple context using a dataclass
@dataclass
class UserContext:
    username: str
    email: str | None = None

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

@function_tool()
async def search(local_context: RunContextWrapper[UserContext], query: str) -> str:
    import time
    time.sleep(30)  # Simulating a delay for the search operation
    return "No results found."

# A tool function that accesses local context via the wrapper
async def special_prompt(special_context: RunContextWrapper[UserContext], agent: Agent[UserContext]) -> str:
    # who is user?
    # which agent
    print(f"\nUser: {special_context.context},\n Agent: {agent.name}\n")
    return f"You are a math expert. User: {special_context.context.username}, Agent: {agent.name}. Please assist with math-related queries."

math_agent: Agent = Agent(name="Genius", instructions=special_prompt, tools=[search])



async def main():
    # Create your context object
    user_info = UserContext(username="abdullah")
    result = await Runner.run(math_agent, "search for the best math tutor in my area", run_config=run_config,context=user_info)
    print(result.final_output)

asyncio.run(main())    