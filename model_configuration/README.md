# 🤖 Agent, Run, and Global Level Examples — Gemini 2.5 Flash

This document explains how to use **Agent Level**, **Run Level**, and **Global Level** settings with the OpenAI Agents SDK using Google Gemini 2.5 Flash.

---

## 🔹 Agent Level

**Definition:** Settings specific to an **individual agent**. Controls personality, creativity, and tool usage.

**Examples:**
```python
agent_cold = Agent(
    name="Cold Agent",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(temperature=0.1)
)

agent_hot = Agent(
    name="Hot Agent",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(temperature=1.9)
)
```
- Temperature controls creativity (0.0 → 2.0)
- Each agent can have different behavior.

---

## 🔹 Run Level

**Definition:** Settings applied **when executing the agent** via `RunConfig`. Controls model selection, provider, tracing, etc.

**Example:**
```python
llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

run_config = RunConfig(
    model=llm_model,
    model_provider=external_client,
)

result = await Runner.run(agent_cold, question, run_config=run_config)
```
- RunConfig allows you to **control execution parameters** per run.
- Does **not** include temperature or tool_choice.

---

## 🔹 Global Level

**Definition:** Settings applied **universally** across all agents and runs. Useful for defaults or shared configurations.

**Example:**
```python
set_tracing_disabled(disabled=True)
set_default_openai_api("chat_completions")
set_default_openai_client(external_client)
```
- Disables tracing globally.
- Sets default OpenAI API and client for all agents.

---

## 🔹 Tool Choice (Agent Level)

Controls how agents decide to use attached tools:

| Tool Choice | Behavior |
|------------|---------|
| auto | Agent decides automatically |
| required | Agent must use tool if relevant |
| none | Agent never uses tools |

**Example:**
```python
agent_auto = Agent(name="Auto", tools=[calculate_area], model_settings=ModelSettings(tool_choice="auto"))
agent_required = Agent(name="Required", tools=[calculate_area], model_settings=ModelSettings(tool_choice="required"))
agent_none = Agent(name="None", tools=[calculate_area], model_settings=ModelSettings(tool_choice="none"))
```
- `Auto` → agent decides
- `Required` → agent must use tool
- `None` → agent ignores tools

---

## 💡 Tips & Recommendations

- **Agent Level:** Always define personality, temperature, and tool usage here.
- **Run Level:** Control model selection, provider, and execution per run.
- **Global Level:** Use for defaults like API client, tracing, or logging.
- Combine these levels to **fine-tune behavior per agent and per execution**.