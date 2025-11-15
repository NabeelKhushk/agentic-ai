# 🔧 Tool Calling Example (Gemini + OpenAI Agents SDK)

This example demonstrates **auto tool-calling** in the OpenAI Agents SDK using the Gemini model.  
The agent automatically decides when to call tools because `tool_choice` defaults to **auto**.

---

## 🚀 Overview

In this example:

- You define two tools: `multiply` and `sum`.
- You instruct the agent to **always use tools for math**.
- Even though you didn’t specify `tool_choice`, the default (`auto`) is applied.
- The agent chooses **which tool to call first**, according to DMAS rules.

---

## 📌 Code (Full Example)

```python
import os
from dotenv import load_dotenv, find_dotenv

from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner, function_tool, set_tracing_disabled

# 0. Load environment variables
load_dotenv(find_dotenv())

# Disable tracing
set_tracing_disabled(disabled=True)

# 1. Define the Gemini provider
external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 2. Define the model
llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

# 3. Run config
run_config = RunConfig(
    model=llm_model,
    model_provider=external_client,
    tracing_disabled=True
)

# 4. Tools
@function_tool
def multiply(a: int, b: int) -> int:
    return a * b

@function_tool
def sum(a: int, b: int) -> int:
    return a + b

# 5. Agent with tools
agent = Agent(
    name="Assistant",
    instructions=(
        "You are a helpful assistant. "
        "Always use tools for math questions. Always follow DMAS rule. "
        "Explain answers clearly for beginners."
    ),
    tools=[multiply, sum],
)

# 6. Run the agent
prompt = "what is 19 + 23 * 2?"
result = Runner.run_sync(agent, prompt, run_config=run_config)

print("\n🤖 CALLING AGENT\n")
print(result.final_output)
```

---

## 🧠 How Tools Are Called

Since you did **not specify**:

```python
model_settings=ModelSettings(tool_choice="required")
```

The SDK uses the default:

### ✅ **`tool_choice="auto"`**

This means:

| Behavior | Result |
|---------|--------|
| Agent decides *when* to use tools | ✔️ |
| Agent decides *which* tool to call first | ✔️ |
| Instructions can force tool usage | ✔️ |
| Tools ignored only if irrelevant | ✔️ |

Because your instructions say:

> “Always use tools for math questions”

The agent **always** calls a tool.

---

## 🧮 Why It Calls Both Tools?

The query:

```
19 + 23 * 2
```

DMAS order:

1. **23 * 2** → requires the `multiply` tool  
2. **19 + result** → requires the `sum` tool  

Thus the model:

1. Calls `multiply(a=23, b=2)`
2. Calls `sum(a=19, b=<multiplication_result>)`
3. Returns the final answer

---

## 📦 Summary

| Feature | Value |
|--------|--------|
| Tool Choice | **auto (default)** |
| Tools Used | `multiply`, `sum` |
| Why Tools Used | Instructions enforced it |
| Math Flow | DMAS → multiply → sum |

---
