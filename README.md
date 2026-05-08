# Autonomous Multi-Agent Financial Reasoning System

An agentic financial analysis pipeline built using LangGraph, LangChain, Groq LLMs, and Tavily Search.

The system decomposes investment analysis into multiple specialized agents that collaborate through a shared graph state to produce a final investment decision.

---

# Architecture Overview

<img width="1326" height="607" alt="image" src="https://github.com/user-attachments/assets/35bb0855-9124-4d31-be87-994535c64108" />

---

# Features

* Multi-agent orchestration using LangGraph
* Shared typed graph state
* Parallel bull vs bear reasoning
* Tavily-powered web research
* Structured outputs using Pydantic
* Critic-based decision synthesis
* Modular agent architecture
* Financial sentiment and risk analysis

---

# Tech Stack

| Component          | Technology        |
| ------------------ | ----------------- |
| Orchestration      | LangGraph         |
| LLM Framework      | LangChain         |
| LLM Provider       | Groq              |
| Search Tool        | Tavily Search API |
| Structured Outputs | Pydantic          |
| Language           | Python            |

---

# Project Structure

```text
app/
│
├── agents/
│   ├── planner.py
│   ├── search_agent.py
│   ├── bull.py
│   ├── bear.py
│   └── critic.py
│
├── orchestration/
│   └── pipeline.py
│
├── schemas/
│   ├── state.py
│   └── output.py
│
├── utils/
│   └── llm.py
│
└── main.py
```

---

# Agent Responsibilities

## Planner Agent

* Understands user query
* Generates research direction
* Creates investigation strategy
* Optimizes downstream search process

## Search Agent

* Performs Tavily web search
* Retrieves financial evidence
* Collects relevant market data
* Stores search results in graph state

## Bull Agent

* Produces bullish investment thesis
* Identifies upside catalysts
* Generates structured confidence score
* Returns detailed positive reasoning

## Bear Agent

* Produces bearish investment thesis
* Identifies downside risks
* Evaluates valuation concerns
* Returns structured negative reasoning

## Critic Agent

* Compares bull and bear arguments
* Aggregates confidence scores
* Resolves conflicting evidence
* Produces final investment decision

---

# Shared Graph State

The system uses a centralized shared state for agent communication.

```python
class GraphState(TypedDict):
    query: str

    plan: str
    search_data: dict

    bull_case: dict
    bear_case: dict

    critique: dict
    final_decision: str
```

---

# Structured Outputs

The agents generate structured outputs using Pydantic schemas.

Example:

```python
{
    "score": 8,
    "confidence": 0.82,
    "reasoning": "NVIDIA dominates AI infrastructure..."
}
```

This enables:

* deterministic downstream processing
* confidence aggregation
* machine-readable reasoning
* cleaner orchestration

---

# Example Output

```text
==================================================
                INVESTMENT ANALYSIS
==================================================

QUERY:
Should I invest in NVIDIA?

==================== BULL CASE ====================

Score: 8/10
Confidence: 0.8

Reasoning:
Strong AI growth, dominant GPU ecosystem,
and positive analyst sentiment.

==================== BEAR CASE ====================

Score: 6/10
Confidence: 0.7

Reasoning:
High valuation, macroeconomic risk,
and increasing competition.

===================== CRITIQUE =====================

Risk Level: MEDIUM
Confidence: 0.81

Reasoning:
Bullish AI tailwinds outweigh near-term risks,
though valuation remains elevated.

================= FINAL DECISION =================

BUY

==================================================
```

---

# Installation

## Clone Repository

```bash
git clone <repo_url>
cd <repo_name>
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
```

---

# Running the Project

```bash
python -m app.main
```

---

# Future Improvements

* Conditional routing
* Reflection/self-correction loops
* Memory & checkpointing
* Streaming outputs
* Supervisor agents
* Portfolio-level analysis
* Historical financial data integration
* Multi-tool orchestration
* Evaluation pipelines
* Real-time market feeds

---

# Key Concepts Demonstrated

* Agentic workflows
* Shared state orchestration
* Multi-agent collaboration
* Parallel execution
* Tool-augmented LLMs
* Structured reasoning pipelines
* Decision synthesis systems

---

# Disclaimer

This project is for educational and research purposes only and does not constitute financial advice.
