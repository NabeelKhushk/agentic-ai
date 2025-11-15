import asyncio
import os
from dotenv import load_dotenv, find_dotenv

from agents import Agent, AsyncOpenAI, ModelSettings, OpenAIChatCompletionsModel, RunConfig, Runner, function_tool, set_tracing_disabled

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

# 🛠️ Simple tool for learning
@function_tool
def calculate_area(length: float, width: float) -> str:
    """Calculate the area of a rectangle."""
    area = length * width
    return f"Area = {length} × {width} = {area} square units"

agent_cold = Agent(
        name="Cold Agent",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(temperature=0.1),
        
    )
    
agent_hot = Agent(
    name="Hot Agent",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(temperature=1.9),
)

agent_auto = Agent(
        name="Auto",
        tools=[calculate_area],
        model_settings=ModelSettings(tool_choice="auto"),
        
    )
    
agent_required = Agent(
    name="Required",
    tools=[calculate_area],
    model_settings=ModelSettings(tool_choice="required"),
    
)

agent_none = Agent(
    name="None",
    tools=[calculate_area],
    model_settings=ModelSettings(tool_choice="none"),
    
)

async def main():
    """Learn Model Settings with simple examples."""
    # 🎯 Example 1: Temperature (Creativity Control)
    print("\n❄️🔥 Temperature Settings")
    print("-" * 30)

    question = "Tell me about AI in 2 sentences"
    
    print("Cold Agent (Temperature = 0.1):")
    cold_result = await Runner.run(agent_cold, question, run_config=run_config)
    print(cold_result.final_output)

    print("\nHot Agent (Temperature = 1.9):")
    hot_result = await Runner.run(agent_hot, question, run_config=run_config)
    print(hot_result.final_output)

    question = "What's the area of a 5x3 rectangle?"

    print("Auto Tool Choice:")
    result_auto = await Runner.run(agent_auto, question, run_config=run_config)
    print(result_auto.final_output)
    
    print("\nRequired Tool Choice:")
    result_required = await Runner.run(agent_required, question, run_config=run_config)
    print(result_required.final_output)

    print("\nNone Tool Choice:")
    result_none = await Runner.run(agent_none, question, run_config=run_config)
    print(result_none.final_output)
    
    print("\n💡 Notice: Auto = decides, Required = must use tool")

asyncio.run(main())    