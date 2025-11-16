# 🤖 Agentic AI Demo — Context-Aware Async Agent using Gemini 2.5-Flash


This project demonstrates how to run an **Agent** using the **OpenAI Agents SDK** while calling the **Gemini API (OpenAI-compatible endpoint)**.

It includes:
- Async agent execution  
- Context-aware tool calling  
- Dataclass-based user context  
- Gemini 2.5 Flash as the backend model  

---

## 🚀 Features

- 🔗 **AsyncOpenAI** client using Gemini’s OpenAI-compatible REST interface  
- 🧩 **Dataclass context (`UserInfo`) attached to the agent**  
- 🔧 **Tool calling** using `@function_tool`  
- ⚡ Fully async, powered by `asyncio`  
- 🛡️ Clean, minimal `RunConfig` structure  

---

## 📦 Full Example Code

```python
import asyncio
from dataclasses import dataclass
import os
from dotenv import load_dotenv, find_dotenv

from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, RunContextWrapper, Runner, function_tool

# 0. Load environment variables
load_dotenv(find_dotenv())

# Define a simple context using a dataclass
@dataclass
class UserInfo:  
    name: str
    uid: int

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

# A tool function that accesses local context via the wrapper
@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:  
    return f"User {wrapper.context.name} is 47 years old"

# 5. Create Agent
agent = Agent[UserInfo](
    name="Assistant",
    tools=[fetch_user_age]    
)

async def main():
    # Create your context object
    user_info = UserInfo(name="Nabeel", uid=123)  
    result = await Runner.run(
        agent, 
        "Hello, What is the age of the user?",
        run_config=run_config,
        context=user_info
    )
    print(result.final_output)

asyncio.run(main())