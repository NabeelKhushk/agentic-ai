# 🧬 Agent Cloning with Gemini 2.5-Flash

This example demonstrates **Agent Cloning** using the **OpenAI Agents SDK**.  
Agent cloning allows you to create multiple variants of a base agent, each with **different behavior, instructions, or tools**, while reusing the core model.

---

## 🔹 What is Agent Cloning?

- **Agent Cloning** is the process of creating a new agent based on an existing agent (base agent).  
- The clone can inherit all properties of the base agent or override specific ones:
  - **Instructions:** Change how the agent responds (friendly, precise, creative, etc.).  
  - **Tools:** Add, remove, or modify the functions the agent can use.  
  - **Settings:** Modify temperature, creativity, or other model parameters.

---

## 🔹 Types of Cloning in This Code

1. **Basic Cloning**
   - Creates a clone with different instructions.
   - Example: `FriendlyAssistant` is a friendly version of `BaseAssistant`.

2. **Cloning with Different Settings**
   - Adjusts model parameters like `temperature`.
   - Example: `CreativeAssistant` (high creativity) vs `PreciseAssistant` (low creativity).

3. **Cloning with Different Tools**
   - Adds or modifies tools for each clone.
   - Example: `WeatherAssistant` has both math and weather tools; `MathAssistant` only has math tools.

4. **Shared vs Independent Clones**
   - **Shared clone:** Shares tool references with base agent; changes in base affect the clone.  
   - **Independent clone:** Has its own tool list; changes in base do not affect it.

5. **Multiple Clones from One Base**
   - Demonstrates creating several specialized variants (creative, precise, friendly, professional) from a single base agent.

---

## 🔹 What Happens in the Code

1. **Setup**
   - Loads `.env` and retrieves Gemini API key.
   - Creates a base LLM model using `gemini-2.5-flash`.

2. **Create Base Agent**
   - Base agent has default instructions and optional tools.

3. **Clone Agents**
   - Multiple clones are created from the base agent with different:
     - Instructions (friendly, precise, creative, professional)
     - Tools (math, weather)
     - Model settings (temperature for creativity)

4. **Test Agents**
   - Each agent or clone is queried with the same prompt to observe differences in behavior and output.

5. **Demonstrate Shared vs Independent Tools**
   - Shows that shared clones reflect changes to the base agent’s tools.
   - Independent clones maintain their own tool set.

---

## ⚡ Summary

- Agent cloning lets you **rapidly create multiple specialized assistants** from a single base.  
- You can experiment with **personality, creativity, and tool availability** for each clone.  
- This code provides practical examples of **friendly, creative, precise, professional, math, and weather agents** to illustrate cloning in action.
