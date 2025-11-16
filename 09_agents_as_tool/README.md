# 📝 Writing Coach AI — Agent Tools Demo (Gemini 2.5-Flash)

This repository demonstrates how to build a **Writing Coach agent** that uses two **specialist agents as tools**:  
a **Spanish Translator** and a **Summarizer**.  
The orchestrator agent decides whether to call a tool or answer directly, using the OpenAI Agents SDK with **Gemini 2.5-Flash**.

---

## 🚀 What This Example Shows

- Creating **specialized mini-agents** (translator, summarizer)
- Turning agents into **tools** using `.as_tool()`
- Building an **orchestrator agent** that:
  - Chooses a tool when needed  
  - Or answers by itself  
- Running fully **async** workflows
- Clear demonstration of **agent-tool composition**

---

## 📌 How the System Works

### 1️⃣ Setup and Model  
The script loads environment variables and initializes a Gemini 2.5-Flash model using `AsyncOpenAI` + OpenAI-compatible API.

### 2️⃣ Specialist Agents  
Two small agents are created:

- **Spanish Translator** → Always outputs Spanish  
- **Summarizer** → Produces exactly 2 bullet points  

These are intentionally simple and purpose-built.

### 3️⃣ Convert Specialists into Tools  
Using `.as_tool()`, each specialist is wrapped as a tool:

- `translate_to_spanish`
- `summarize_text`

This allows another agent to call them programmatically.

### 4️⃣ Orchestrator (Writing Coach)  
A main “coach” agent is created with logic:

- If prompt contains *“translate to Spanish”* → call translator tool  
- If prompt contains *“summarize”* → call summarizer tool  
- Else → give general writing advice  

The coach keeps the mic — tools run in the background and return results back to the coach.

### 5️⃣ Running Examples  
The script demonstrates three flows:

A) **Tool call: Translation**  
B) **Tool call: Summarization**  
C) **Direct coaching without tools**

---

## 🧠 Summary

This example teaches how to:

- Build **small specialist agents**
- Convert them to **tools**
- Use an **orchestrator agent** to intelligently route tasks
- Combine agents into a **cooperative AI system**

Perfect for building writing assistants, multi-skill copilots, or extensible agent ecosystems.

---
