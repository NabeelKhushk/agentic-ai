Agent Framework Demo: Gemini via OpenAI API
This document provides a guide for running a minimal Python example that integrates the Gemini 2.5 Flash model into an agent-based workflow using an OpenAI-compatible API.

This approach allows developers to utilize Google's powerful Gemini models within existing agent frameworks and libraries built for the OpenAI ecosystem.

🚀 Getting Started
Follow these steps to set up and run the example.

Prerequisites
Python 3.8+

A Gemini API Key.

Installation
Install the necessary Python packages using pip:

Bash

pip install python-dotenv openai [your_agent_framework]
Note: Replace [your_agent_framework] with the actual package providing Agent, Runner, etc.

📝 Environment Variables
Create a file named .env in the project root and set your API key:

# .env file
GEMINI_API_KEY="your_api_key_here"
Security Warning: Never commit your .env file or API keys directly to GitHub.

Running the Program
Save your Python code as main.py and execute the script:

Bash

python main.py
Expected Output:

I'm doing great, thank you for asking! How can I help you today?
🔑 Key Components
The core integration is achieved by configuring the client to redirect to the Gemini API endpoint.

1. Model Provider (external_client)
This defines the external LLM provider. We use the standard AsyncOpenAI client but point it to the Gemini gateway URL.

Example:

Python

external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
Supported Providers: Gemini via OpenAI-compatible API.

2. Model Definition (llm_model)
This specifies which Gemini model to use.

Example:

Python

llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)
3. Agent Instructions
The Agent is given a defined role and conditional tool use instructions.

Instructions:

"You are a helpful assistant to answer the questions. But if user asks about weather, use the get_weather tool."

💡 Summary of Code Flow
The Python script executes the workflow in these sequential steps:

Loads environment variables (dotenv).

Initializes the AsyncOpenAI client pointing to the Gemini base URL.

Defines the gemini-2.5-flash model configuration.

Sets up the RunConfig.

Creates the Agent with its defined instructions.

Runs the agent using Runner.run with the initial prompt ("Hello, how are you?").

Prints the final output from the model.