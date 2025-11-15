# 🌡️ Temperature & Tool Settings

Hello Agent allows you to **control creativity and tool usage** via `model_settings` in each agent.

---

### 🔹 Temperature (Creativity Control)

**Definition:** Temperature controls **how random or creative** the agent’s responses are.  

**Range:** `0.0 → 2.0`  

**Behavior Table:**

| Temperature | Behavior | Example |
|------------|---------|---------|
| 0.0 – 0.3 | Cold / Deterministic | “AI is the simulation of human intelligence by machines.” |
| 0.4 – 0.7 | Slightly Creative | Adds minor variations in phrasing |
| 0.8 – 1.5 | Creative / Exploratory | “AI can be like a virtual teacher guiding your learning adventures.” |
| 1.6 – 2.0 | Very Creative / Unpredictable | “AI is like a cat riding a rocket, discovering the universe of data!” |

**Usage Example:**
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

---

### 🔹 Tool Choice

Controls **how agents decide to use attached tools** (like Python functions).  

| Tool Choice | Behavior |
|------------|---------|
| `auto` | Agent decides **automatically** when to use a tool |
| `required` | Agent **must use** a tool if relevant |
| `none` | Agent **never uses tools**, even if available |

**Usage Example:**
```python
agent_auto = Agent(
    name="Auto Agent",
    tools=[calculate_area],
    model_settings=ModelSettings(tool_choice="auto")
)

agent_required = Agent(
    name="Required Agent",
    tools=[calculate_area],
    model_settings=ModelSettings(tool_choice="required")
)

agent_none = Agent(
    name="No Tool Agent",
    tools=[calculate_area],
    model_settings=ModelSettings(tool_choice="none")
)
```

---

### 🔹 How It Works Together

- **Cold agent + any tool choice** → factual, low creativity  
- **Hot agent + any tool choice** → imaginative, creative outputs  
- **Tool choice** lets you **control whether external functions are used or ignored**  

💡 **Tip:** Use **temperature** to tune creativity, and **tool_choice** to enforce or relax tool usage for your workflow.