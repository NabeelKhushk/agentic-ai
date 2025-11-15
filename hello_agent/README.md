🤖 Hello Agent — Minimal AI Assistant

Hello Agent is a lightweight AI assistant built using the OpenAI Agents SDK with Google Gemini 2.5 Flash.
It demonstrates how to create an agent that is helpful, responsive, and easily extensible.

✨ Features

💡 LLM Configuration – Connect to Gemini via OpenAI-compatible API

🧠 Agent Setup – Define an agent with custom instructions and personality

⚡ Async Execution – Run the agent asynchronously for smooth responses

🔧 Extensibility – Add tools, workflows, or multi-step reasoning easily

📝 Clean Outputs – Extract final responses programmatically

Use Case: Build predictable, task-focused AI assistants for real-world automation and experimentation.

📂 Project Structure
hello_agent/
│── .venv/                     # Python virtual environment
│── src/
│    └── hello_agent/
│         └── main.py          # Main async agent script
│── .env                       # Environment variables (not committed)
│── requirements.txt            # Python dependencies
└── README.md                  # This file

🔧 Installation
1. Clone the repository
git clone <repo-url>
cd hello_agent

2. Create and activate a virtual environment
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows CMD
.venv\Scripts\activate.bat

3. Install dependencies
pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here


Note: Never commit your .env file to GitHub.

⚙️ Key Components
🔹 1. model_provider

Defines the external LLM provider.

Example:

external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


Supported providers:

Gemini via OpenAI-compatible API

OpenAI GPT models

Claude, LiteLLM, or other custom providers

🔹 2. model

Specifies which LLM the agent will use.

Example:

llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)


Supported models:

Gemini 2.5 Flash

GPT-4.1 / GPT-4.1-mini

GPT-o / GPT-o-mini

Any OpenAI-compatible or custom model

🔹 3. instructions

System-level rules and behavior for the agent.

Example:

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant to answer questions."
)


Defines the agent’s personality, tone, and constraints.

🔹 4. run_config

Controls agent execution.

Example:

run_config = RunConfig(
    model=llm_model,
    model_provider=external_client,
    tracing_disabled=True
)

Setting	Behavior
model	Specifies the LLM model used
model_provider	Defines the API client
tracing_disabled	Disables debug/tracing info
🔹 5. Async Execution

Example:

result = await Runner.run(agent, "Hello, how are you?", run_config=run_config)
print(result.output_text)

Feature	Behavior
Async	Non-blocking execution using await
Output	result.output_text contains the final message
Metadata	Full RunResult object available if needed
🔹 6. tools (optional)

Functions the agent can call.

Example:

tools=[send_email, fetch_inbox]


Supported tool types:

Python functions (@function_tool)

API/HTTP calls

Database queries

Local utilities

Multi-agent handoffs

📦 Complete Example
import asyncio
import os
from dotenv import load_dotenv, find_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner

# Load environment variables
load_dotenv(find_dotenv())

# LLM Provider
external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model
llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

# Run Configuration
run_config = RunConfig(
    model=llm_model,
    model_provider=external_client,
    tracing_disabled=True
)

# Agent
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant to answer questions."
)

# Run Agent
async def main():
    result = await Runner.run(agent, "Hello, how are you?", run_config=run_config)
    print(result.output_text)

asyncio.run(main())


Expected output:

Hello! I'm doing well, thank you for asking. How can I help you today?

🧠 Key Learnings
Concept	Outcome
External model integration	Gemini via OpenAI-compatible API
Model configuration	OpenAIChatCompletionsModel
Run execution	Controlled via RunConfig
Async workflow	Runner.run() with asyncio
Clean output	Extract response using result.output_text
💡 Summary

Hello Agent provides a clean, minimal starting point to build agentic AI applications.
By configuring the model provider, instructions, run settings, and optional tools, you can transform a generic LLM into a predictable, task-focused AI assistant ready for real-world workflows.