import asyncio
from dataclasses import dataclass
import os
from dotenv import load_dotenv, find_dotenv

from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, RunContextWrapper, Runner, function_tool, handoff

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

# Fitness Coach 
fitness_coach = Agent(
    name="Fitness Coach",
    instructions=(
        "You're a running coach. Ask 1-2 quick questions, then give a week plan. "
        "Keep it simple and encouraging. No medical advice."
    ),
)

# Study Coach
study_coach = Agent(
    name="Study Coach",
    instructions=(
        "You're a study planner. Ask for current routine, then give a 1-week schedule. "
        "Keep steps small and doable."
    ),
)

# Router that decides who should OWN the conversation
router = Agent(
    name="Coach Router",
    instructions=(
        "Route the user:\n"
        "- If message is about running, workout, stamina → handoff to Fitness Coach.\n"
        "- If it's about exams, study plan, focus, notes → handoff to Study Coach.\n"
        "After handoff, the specialist should continue the conversation."
    ),
    handoffs=[study_coach, handoff(fitness_coach)],
)



async def main():
    # ---- Turn 1: user asks about running → should handoff to Fitness Coach
    r1 = await Runner.run(router, "I want to run a 5Km in 8 weeks. Can you help?",run_config=run_config)
    print("\nTurn 1 (specialist reply):\n", r1.final_output)

     # Grab the specialist that actually replied (Fitness Coach)
    specialist = r1.last_agent

    # ---- Turn 2: user answers the coach's follow-up; continue with SAME specialist
    t2_input = r1.to_input_list() + [
        {"role": "user", "content": "Right now I can jog about 2 km, 3 days per week."}
    ]
    r2 = await Runner.run(specialist, t2_input,run_config=run_config)
    print("\nTurn 2 (specialist reply):\n", r2.final_output)

asyncio.run(main())   