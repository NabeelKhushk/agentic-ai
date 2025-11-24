# Advanced Agent Example with Tools, Context, and Conditional Execution

This repository contains a **single-file Python example** demonstrating advanced usage of agentic AI with the OpenAI-compatible Gemini LLM. The example shows how to create agents that can:

- Call **Python function tools** during conversations.
- Use **context-aware execution**, like checking user subscription tiers or admin privileges.
- Implement **conditional tool access**, allowing some tools only for premium users or admins.
- Handle **multi-turn conversations**, remembering the state of the conversation and respecting tool usage rules.
- Stop execution safely after specific tools are called using `StopAtTools`.
- Demonstrate **dynamic routing and handoff** between different agents.

## Key Features

1. **Admin Tools:**  
   Tools like `delete_user` are restricted to users with `is_admin=True`.

2. **Premium Features:**  
   Certain tools, like `get_weather`, are only accessible to premium or enterprise users.

3. **Tool Usage Control:**  
   `StopAtTools` ensures that once a critical tool is used, the agent stops further turns, preventing unsafe operations.

4. **Context Awareness:**  
   Agents can read from `RunContextWrapper` to adapt behavior dynamically based on user roles or conversation state.

5. **LLM Provider:**  
   Uses Gemini 2.5-Flash model via OpenAI-compatible API to power the agents.

This example is **fully runnable**, demonstrating how agents, tools, and context work together to create a robust AI assistant workflow.
