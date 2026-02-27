<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,28&height=170&section=header&text=Multi-Agent%20Research%20Team&fontSize=42&fontAlignY=35&animation=twinkling&fontColor=ffffff&desc=4%20AI%20Agents%20Collaborate%20via%20CrewAI%20%2B%20Claude%20to%20Create%20Content&descAlignY=55&descSize=18" width="100%" />

[![CrewAI](https://img.shields.io/badge/CrewAI_v1.9-Multi_Agent-059669?style=for-the-badge)](.)
[![Claude](https://img.shields.io/badge/Claude_Sonnet-Powered-8B5CF6?style=for-the-badge&logo=anthropic&logoColor=white)](.)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](.)
[![Serper](https://img.shields.io/badge/Serper-Web_Search-FF6B6B?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](.)
[![Railway](https://img.shields.io/badge/Railway-Deployed-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)](.)

**Give it a topic. 4 Claude-powered agents research, analyze, write, and edit — delivering platform-ready content for LinkedIn, Twitter, and newsletters.**

</div>

---

## Why This Exists

Creating content about fast-moving AI topics requires research, analysis, writing, AND editing. Doing all four well takes hours. This system splits the work across 4 specialized AI agents powered by Claude, orchestrated through CrewAI's framework.

Each agent has a defined role, expertise, and output format. The Researcher searches the web. The Analyst extracts insights. The Writer creates platform-specific content. The Editor fact-checks and polishes. They work sequentially — each agent's output becomes the next agent's input.

The result: comprehensive, platform-ready content in minutes instead of hours.

---

## Architecture

```
User: "Latest breakthroughs in AI agents"
         │
         ▼
┌──────────────────────────────────────────────────────────┐
│                  CrewAI Orchestrator                       │
│               (Sequential Process + Claude)                │
│                                                            │
│  ┌──────────────┐       ┌──────────────┐                  │
│  │ 🔍 Researcher │──────→│ 📊 Analyst    │                  │
│  │ • Web search  │       │ • Top 3       │                  │
│  │ • Scraping    │       │   insights    │                  │
│  │ • 3-5 sources │       │ • Trends      │                  │
│  └──────────────┘       └──────┬───────┘                  │
│                                 │                          │
│  ┌──────────────┐       ┌──────▼───────┐                  │
│  │ ✅ Editor     │←──────│ ✍️ Writer     │                  │
│  │ • Fact-check  │       │ • LinkedIn    │                  │
│  │ • Polish      │       │ • Twitter     │                  │
│  │ • Optimize    │       │ • Newsletter  │                  │
│  └──────┬───────┘       └──────────────┘                  │
│         │                                                  │
└─────────┼──────────────────────────────────────────────────┘
          ▼
   Platform-ready content (copy-paste and post)
```

---

## The 4 Agents

| Agent | Role | Tools | LLM | What It Does |
|-------|------|-------|-----|-------------|
| **🔍 Researcher** | Senior Research Analyst | Serper Web Search, Website Scraper | Claude Sonnet | Searches the web for latest news, data, expert opinions, primary sources |
| **📊 Analyst** | Strategic Analyst | None (pure reasoning) | Claude Sonnet | Extracts top 3 insights, identifies trends, finds the unique angle |
| **✍️ Writer** | Content Strategist | None (pure reasoning) | Claude Sonnet | Creates LinkedIn post, Twitter thread, newsletter article — each optimized for platform |
| **✅ Editor** | Senior Editor & Fact Checker | None (pure reasoning) | Claude Sonnet | Verifies claims against research, strengthens hooks, ensures platform best practices |

---

## How It Works

| Step | Agent | Input | Output |
|------|-------|-------|--------|
| **1** | Researcher | User's topic | Research brief with sources, data, expert quotes |
| **2** | Analyst | Research brief | 3 key insights + trend analysis + unique angle + significance score |
| **3** | Writer | Analysis | LinkedIn post + Twitter thread + newsletter section |
| **4** | Editor | All content | Fact-checked, polished, platform-optimized final content |

CrewAI handles the handoff between agents automatically. Each task's output flows into the next as context.

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **CrewAI over custom orchestration** | Industry-standard framework — the one recruiters search for on GitHub |
| **Claude over OpenAI** | All 4 agents explicitly configured with `llm=claude_llm` — no OpenAI dependency |
| **Sequential over hierarchical** | Research must finish before analysis, analysis before writing. Linear flow ensures quality |
| **4 agents (not 2 or 6)** | Maps to real content workflows. Fewer = less nuance. More = diminishing returns |
| **Serper for web search** | Most reliable search API for agents. Free tier with 2,500 searches |
| **Editor as final agent** | Last line of defense — catches hallucinations by cross-referencing original research |

---

## Quick Start

```bash
git clone https://github.com/ajay-automates/multi-agent-research-team.git
cd multi-agent-research-team
pip install -r requirements.txt

export ANTHROPIC_API_KEY="your-key"
export SERPER_API_KEY="your-key"     # Free at serper.dev

# Web UI
python main.py    # http://localhost:8000

# CLI
python crew.py "Latest breakthroughs in AI agents"
```

### Deploy on Railway

1. Connect this repo to Railway
2. Set `ANTHROPIC_API_KEY` and `SERPER_API_KEY`
3. Deploy — Procfile + runtime.txt handle the rest

---

## Example Topics

| Topic | What The Team Produces |
|-------|----------------------|
| "Latest AI agent frameworks — CrewAI vs LangGraph vs AutoGen" | Research brief + comparison + LinkedIn post + Twitter thread + newsletter |
| "OpenAI vs Anthropic — who's winning in 2026?" | Market analysis + strategic insights + hot-take content |
| "MCP (Model Context Protocol) — why every AI engineer needs this" | Technical research + trend analysis + educational content |
| "Top 5 AI tools that launched this week" | Product research + impact analysis + listicle content |

---

## Project Structure

```
multi-agent-research-team/
├── agents.py             # 4 agent definitions with Claude LLM
├── tasks.py              # 4 task definitions (research, analyze, write, edit)
├── crew.py               # CrewAI orchestration + CLI runner
├── main.py               # FastAPI server
├── templates/
│   └── index.html        # Dark-theme UI with pipeline visualization
├── requirements.txt      # CrewAI v1.9+ with tools
├── runtime.txt           # Python 3.12 pin
├── Procfile              # Railway deployment
└── README.md
```

---

## What This Demonstrates

| AI Engineering Skill | Implementation |
|---------------------|----------------|
| **Multi-Agent Orchestration** | 4 agents with defined roles collaborating via CrewAI |
| **Agent Framework (CrewAI)** | Industry-standard framework with sequential process |
| **Custom LLM Configuration** | Claude Sonnet explicitly set as LLM for all agents |
| **Task Delegation & Dependencies** | Sequential pipeline where each task feeds the next |
| **Tool Integration** | Web search (Serper) and scraping assigned to specific agents |
| **Agent Specialization** | Unique expertise, backstory, and constraints per agent |
| **Production Web UI** | FastAPI + real-time pipeline visualization |

---

## Tech Stack

`CrewAI v1.9` `Claude Sonnet (Anthropic)` `FastAPI` `Serper API` `Python 3.12` `Jinja2` `Railway`

---

## Related Projects

| Project | Description |
|---------|-------------|
| [AI Finance Agent](https://github.com/ajay-automates/ai-finance-agent) | Claude tool-calling agent with real-time stock data |
| [Agentic RAG Pipeline](https://github.com/ajay-automates/agentic-rag-pipeline) | Self-correcting RAG with hallucination detection |
| [Multi-Orchestration System](https://github.com/ajay-automates/multi-orchestration-system) | Custom multi-agent system with self-healing infrastructure |

---

<div align="center">

**Built by [Ajay Kumar Reddy Nelavetla](https://github.com/ajay-automates)** · February 2026

*4 agents. 1 topic. Platform-ready content in minutes.*

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,28&height=100&section=footer" width="100%" />

</div>
