import os
from dotenv import load_dotenv, find_dotenv

from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner, function_tool, set_tracing_disabled

# 0. Load environment variables
load_dotenv(find_dotenv())

# 🚫 Disable tracing for clean output (optional for beginners)
set_tracing_disabled(disabled=True)

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

# 🛠️ 4) Define tools (functions wrapped for tool calling)
@function_tool
def multiply(a: int, b: int) -> int:
    """🧮 Exact multiplication (use this instead of guessing math)."""
    return a * b

@function_tool
def sum(a: int, b: int) -> int:
    """➕ Exact addition (use this instead of guessing math)."""
    return a + b

# 🤖 5) Create agent and register tools
agent: Agent = Agent(
    name="Assistant",  # 🧑‍🏫 Agent's identity
    instructions=(
        "You are a helpful assistant. "
        "Always use tools for math questions. Always follow DMAS rule (division, multiplication, addition, subtraction). "
        "Explain answers clearly and briefly for beginners."
    ),
    tools=[multiply, sum],  # 🛠️ Register tools here
)

# 🧪 5) Run the agent with a prompt (tool calling expected)
prompt = "what is 19 + 23 * 2?"
result = Runner.run_sync(agent, prompt,run_config=run_config)

# 📤 Print the final result from the agent
print("\n🤖 CALLING AGENT\n")
print(result.final_output)