# 🤖 Streaming Async AI Agent Demo with Gemini 2.5-Flash

This example demonstrates how to build a **context-aware AI agent** using the **OpenAI Agents SDK** and the **Gemini API**, with a primary focus on **streaming outputs**.  

Streaming allows the agent to **produce events or partial outputs in real-time**, so you can process or display responses as they are generated, instead of waiting for the final output.

---

## 📌 What is Streaming?

- **Streaming** means the agent sends data in chunks or events as it generates it.  
- Ideal for **long-running tasks**, **interactive assistants**, or **real-time dashboards**.  
- Instead of waiting for the final response, your application can **react to each event as it arrives**.

---

## 📖 What This Code Does

1. **Loads environment variables** and the Gemini API key.  
2. Defines a **user context (`UserContext`)** dataclass with `username` and optional `email`.  
3. Connects to the **Gemini 2.5-Flash model** asynchronously using `AsyncOpenAI`.  
4. Sets up a **run configuration** with tracing disabled.  
5. Defines a **tool function (`search`)** that simulates a delayed search operation.  
6. Defines a **special prompt** function to provide dynamic instructions for the agent based on the user context.  
7. Creates an **Agent instance** named `"Genius"` with the special prompt and tools.  
8. Runs the agent using **`Runner.run_streamed`**:
   - Sends a query `"search for the best math tutor in my area"`.  
   - Streams the output **event by event**, printing results in real-time.  

This demonstrates how the agent can **use tools**, **access context**, and **stream outputs dynamically**.

---

## ⚡ Summary

- This code is a **template for building streaming, context-aware AI agents**.  
- It allows **real-time interaction** with users while executing tasks.  
- Tools and context make the agent **flexible and dynamic**.  
- Streaming output is useful for **dashboards, assistants, and live systems** where instant feedback is important.
