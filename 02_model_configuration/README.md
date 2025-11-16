# 🤖 Gemini 2.5 Flash — Agent Examples

This document provides **three examples** demonstrating different ways to define and run agents using the OpenAI Agents SDK with Google Gemini 2.5 Flash.

---

## 🔹 Example 1 — Inline Model in Agent

**Description:** Define the **LLM model directly inside the Agent**. Useful for quick experiments.

```python
agent = Agent(
    name="Assistant",
    instructions="You only respond in haikus.",
    model=OpenAIChatCompletionsModel(
        model="gemini-2.5-flash",
        openai_client=external_client
    ),
)

result = await Runner.run(
    agent,
    "Tell me about recursion in programming."
)
print(result.final_output)
```

**Notes:**
- Model is tied **directly to this agent**.
- No separate `RunConfig` needed.

---

## 🔹 Example 2 — Using RunConfig

**Description:** Define the model separately and use **RunConfig** during execution.

```python
llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

run_config = RunConfig(
    model=llm_model,
    model_provider=external_client,
)

agent = Agent(
    name="Assistant",
    instructions="You only respond in haikus."
)

result = await Runner.run(
    agent,
    "Tell me about recursion in programming.",
    run_config=run_config
)
print(result.final_output)
```

**Notes:**
- RunConfig separates **model definition** from **execution settings**.
- Useful for **advanced setups** or multiple agents sharing the same model.

---

## 🔹 Example 3 — Using Default Client & API

**Description:** Set global defaults and specify the model by name in the agent.

```python
set_default_openai_api("chat_completions")
set_default_openai_client(external_client)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="gemini-2.5-flash"
)

result = await Runner.run(agent, "Hello")
print(result.final_output)
```

**Notes:**
- Uses **global defaults** for API and client.
- Simplifies agent creation by just specifying the model name.
- Ideal when multiple agents share the same client.

---

## 🔹 Comparison Table

| Example | Model Definition | RunConfig | When to Use |
|--------|----------------|-----------|------------|
| 1 | Inline in Agent | Not used | Quick tests, simple setups |
| 2 | Separate OpenAIChatCompletionsModel | Used | Advanced setups, shared models |
| 3 | By name with default client | Not used | Multiple agents sharing client |

💡 **Tip:** Choose based on **complexity** and