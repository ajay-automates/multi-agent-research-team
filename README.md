<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,28&height=170&section=header&text=Multi-Agent%20Research%20Team&fontSize=42&fontAlignY=35&animation=twinkling&fontColor=ffffff&desc=4%20AI%20Agents%20Collaborate%20via%20CrewAI%20to%20Research%2C%20Analyze%2C%20Write%20%26%20Edit&descAlignY=55&descSize=18" width="100%" />

[![CrewAI](https://img.shields.io/badge/CrewAI-Multi_Agent-059669?style=for-the-badge)](.)
[![Claude](https://img.shields.io/badge/Claude_Sonnet-LLM-8B5CF6?style=for-the-badge&logo=anthropic&logoColor=white)](.)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](.)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](.)
[![Serper](https://img.shields.io/badge/Serper-Web_Search-FF6B6B?style=for-the-badge)](.)
[![Railway](https://img.shields.io/badge/Railway-Deploy-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)](.)

**Give it a topic. 4 agents research, analyze, write, and edit — delivering platform-ready content for LinkedIn, Twitter, and newsletters.**

</div>

---

## Why This Exists

Creating content about fast-moving AI topics requires research, analysis, writing, AND editing. Doing all four well takes hours. This system splits the work across 4 specialized AI agents that collaborate through CrewAI's orchestration framework.

Each agent has a defined role, expertise, and output format. The Researcher finds information. The Analyst extracts insights. The Writer creates platform-specific content. The Editor fact-checks and polishes. They work sequentially — each agent's output becomes the next agent's input.

---

## Architecture

```
User provides topic: "Latest AI agent frameworks"
         │
         ▼
┌─────────────────────────────────────────────────────────┐
│                    CrewAI Orchestrator                    │
│                  (Sequential Process)                     │
│                                                           │
│  ┌─────────────┐     ┌─────────────┐                     │
│  │  🔍 Agent 1  │────→│  📊 Agent 2  │                     │
│  │  Researcher  │     │  Analyst     │                     │
│  │  • Web search│     │  • Key insights│                   │
│  │  • Scraping  │     │  • Trends     │                    │
│  └─────────────┘     └──────┬──────┘                     │
│                              │                             │
│  ┌─────────────┐     ┌──────▼──────┐                     │
│  │  ✅ Agent 4  │←────│  ✍️ Agent 3  │                     │
│  │  Editor      │     │  Writer      │                     │
│  │  • Fact check│     │  • LinkedIn   │                    │
│  │  • Polish    │     │  • Twitter    │                    │
│  └──────┬──────┘     └─────────────┘                     │
│         │                                                 │
└─────────┼─────────────────────────────────────────────────┘
          ▼
   Platform-ready content
```

---

## The 4 Agents

| Agent | Role | Tools | What It Does |
|-------|------|-------|-------------|
| **🔍 Researcher** | Senior Research Analyst | Web Search, Scraping | Searches the web for latest news, data, expert opinions |
| **📊 Analyst** | Strategic Analyst | None (reasoning) | Extracts top 3 insights, identifies trends, finds unique angles |
| **✍️ Writer** | Content Strategist | None (reasoning) | Creates LinkedIn post, Twitter thread, newsletter article |
| **✅ Editor** | Senior Editor | None (reasoning) | Fact-checks, strengthens hooks, ensures platform best practices |

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **CrewAI over custom orchestration** | Industry-standard framework recruiters search for |
| **Sequential over hierarchical** | Research → Analysis → Writing → Editing requires linear flow |
| **4 agents (not 2 or 6)** | Maps to real content workflows with optimal specialization |
| **Serper for web search** | Most reliable search API. Real Google results |
| **Editor as final agent** | Catches hallucinations by cross-referencing original research |

---

## Quick Start

```bash
git clone https://github.com/ajay-automates/multi-agent-research-team.git
cd multi-agent-research-team
pip install -r requirements.txt

export ANTHROPIC_API_KEY="your-key"
export SERPER_API_KEY="your-key"

# Web UI
python main.py    # http://localhost:8000

# CLI
python crew.py "Latest breakthroughs in AI agents"
```

---

## Project Structure

```
multi-agent-research-team/
├── agents.py             # 4 agent definitions (roles, goals, tools)
├── tasks.py              # 4 task definitions (research, analyze, write, edit)
├── crew.py               # CrewAI orchestration + CLI runner
├── main.py               # FastAPI server
├── templates/
│   └── index.html        # Web UI with pipeline visualization
├── requirements.txt
├── Procfile
└── README.md
```

---

## What This Demonstrates

| AI Engineering Skill | Implementation |
|---------------------|----------------|
| **Multi-Agent Orchestration** | 4 agents collaborating via CrewAI |
| **Agent Framework (CrewAI)** | Industry-standard framework |
| **Task Delegation** | Sequential pipeline, each task feeds the next |
| **Tool Integration** | Web search + scraping assigned to specific agents |
| **Agent Specialization** | Unique expertise, backstory, and constraints per agent |

---

## Tech Stack

`CrewAI` `Claude (Anthropic)` `FastAPI` `Serper API` `Python` `Jinja2` `Railway`

---

## Related Projects

| Project | Description |
|---------|-------------|
| [AI Finance Agent](https://github.com/ajay-automates/ai-finance-agent) | Claude tool-calling agent with real-time stock data |
| [AI Support Agent](https://github.com/ajay-automates/ai-support-agent) | RAG chatbot with LangSmith observability |
| [Multi-Orchestration System](https://github.com/ajay-automates/multi-orchestration-system) | Custom multi-agent system with self-healing |

---

<div align="center">

**Built by [Ajay Kumar Reddy Nelavetla](https://github.com/ajay-automates)** · February 2026

*4 agents. 1 topic. Platform-ready content in minutes.*

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,28&height=100&section=footer" width="100%" />

</div>
