from dataclasses import dataclass
from agents import (
    Agent,
    AgentBase,
    OpenAIChatCompletionsModel,
    RunConfig,
    RunContextWrapper,
    Runner,
    function_tool,
    StopAtTools,
    AsyncOpenAI,
    set_tracing_disabled,
)
from dotenv import find_dotenv, load_dotenv
import asyncio
import os

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
    model_provider=external_client
)

set_tracing_disabled(disabled=True)


@function_tool
def get_user_data(user_id: str) -> str:
    """Looks up user data."""
    return f"Data for {user_id}: Name - Alex, Role - user"

@dataclass
class UserScope:
    is_admin: bool

async def is_admin(ctx: RunContextWrapper[UserScope], agent: AgentBase[UserScope]) -> bool:
    print("Checking if admin allowed...", ctx.context)
    return True if ctx.context.is_admin else False

# TODO 1: Make this an admin-only tool using `is_enabled`.
@function_tool(is_enabled=is_admin)
def delete_user(user_id: str) -> str:
    """Deletes a user. This is a final action."""
    return f"User {user_id} has been deleted."


admin_agent = Agent(
    name="Admin Agent",
    instructions="Help manage users. First get data, then delete if asked.",
    tools=[get_user_data, delete_user],
    model=llm_model,
    # TODO 2: Make the agent stop immediately after a user is deleted
    # using `tool_use_behavior` and `StopAtTools`.
    tool_use_behavior=StopAtTools(stop_at_tool_names=["delete_user"]),
)


async def main():
    print("--- Running as a regular user ---")
    result_user = await Runner.run(
        admin_agent, "Please delete user client_456.", context=UserScope(is_admin=False)
    )
    print(f"Final Output: {result_user.final_output}")

    print("\n--- Running as an admin ---")
    # TODO 3: Set max_turns to 3 for this run as a safety limit.
    result_admin = await Runner.run(
        admin_agent,
        "Get data for user_123 and then delete them.",
        context=UserScope(is_admin=True),
        max_turns=3,
    )
    print(f"Final Output: {result_admin.final_output}")


asyncio.run(main())