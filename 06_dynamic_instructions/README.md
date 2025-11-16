# 🤖 Dynamic Instruction Agents — Simple Explanation

This example shows how to build **multiple dynamic AI agents** using the OpenAI Agents SDK (with Gemini as the backend). Each agent changes its behavior based on different conditions such as message history, time, or internal memory.

---

## 🚀 What This Code Demonstrates

This single file teaches five different ways an AI agent can behave dynamically:

1. **Basic Dynamic Agent** → Always friendly and helpful  
2. **Context-Aware Agent** → Behavior changes based on message count  
3. **Time-Based Agent** → Morning/afternoon/evening tone  
4. **Stateful Agent** → Remembers how many times you interacted  
5. **Context Explorer Agent** → Reads messages, tools, and agent info

It also shows how to use:

- `AsyncOpenAI` (Gemini backend)
- `RunConfig`  
- `RunContextWrapper`  
- Dynamic `instructions` functions  
- Async execution using `asyncio`

---

## 🧩 Step-by-Step Explanation of the Code

### 1. **Load Env Variables**
Loads `.env` (to fetch `GEMINI_API_KEY`).

### 2. **User Context Dataclass**
A simple structure to hold user info.

### 3. **Setup Gemini with OpenAI-Compatible API**
Uses `AsyncOpenAI` to talk to Gemini through the OpenAI Agents SDK.

### 4. **Choose the Model**
`gemini-2.5-flash` is selected for chat completions.

### 5. **Run Configuration**
Defines:
- the model
- the client
- tracing options

### 6. **Define Dynamic Instruction Functions**
These functions generate instructions at runtime:
- Some check message count  
- Some check current time  
- Some maintain internal state (memory)  
- Some inspect the context  

Each function returns a string that becomes the “instructions” the agent follows.

### 7. **Create Five Agents**
Each agent is built with:
- a name  
- its own dynamic instruction generator  

### 8. **Run All Examples Inside `main()`**
The `main()` function runs every agent example:
- Basic dynamic  
- Context-aware (multiple messages)  
- Time-aware  
- Stateful memory agent  
- Context explorer  

The output gets printed in the console.

### 9. **Execute the Program**
`asyncio.run(main())` starts everything.

---

## 🏁 Summary

This script teaches how to create **dynamic, context-sensitive, memory-aware AI agents** using the OpenAI Agents SDK with a Gemini backend. Each agent behaves differently depending on logic you define—message count, time of day, internal memory, or contextual data. It's a clean template for building smart, adaptable agents for real-world applications.

