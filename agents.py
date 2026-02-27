"""
Multi-Agent Research Team - Agent Definitions
4 specialized agents that collaborate via CrewAI using Claude.
"""

from crewai import Agent, LLM
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
import os

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Use Claude as the LLM for all agents
claude_llm = LLM(
    model="anthropic/claude-sonnet-4-20250514",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)


def create_researcher():
    return Agent(
        role="Senior Research Analyst",
        goal="Find the most relevant, recent, and accurate information on the given topic",
        backstory=(
            "You are an expert research analyst with 15 years of experience. "
            "You excel at finding information others miss, identifying primary sources, "
            "and distinguishing credible data from noise. You focus on recent developments."
        ),
        tools=[search_tool, scrape_tool],
        llm=claude_llm,
        verbose=True,
        allow_delegation=False,
        max_iter=5,
    )


def create_analyst():
    return Agent(
        role="Strategic Analyst",
        goal="Analyze research findings to extract key insights, identify patterns, and form conclusions",
        backstory=(
            "You are a strategic analyst who synthesizes complex information into clear, "
            "actionable insights. You identify trends, spot contradictions, and rank findings "
            "by importance. You always think about why this matters for the audience."
        ),
        tools=[],
        llm=claude_llm,
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )


def create_writer():
    return Agent(
        role="Content Strategist and Writer",
        goal="Transform analysis into engaging, platform-ready content that drives engagement",
        backstory=(
            "You are a content strategist who has grown multiple tech accounts to 100K+ followers. "
            "You understand what makes content viral on LinkedIn, Twitter, and newsletters. "
            "You write with authority, use hooks that stop the scroll, and include specific data points."
        ),
        tools=[],
        llm=claude_llm,
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )


def create_editor():
    return Agent(
        role="Senior Editor and Fact Checker",
        goal="Review all content for accuracy, clarity, engagement, and platform best practices",
        backstory=(
            "You are a senior editor at a top tech publication. You catch factual errors, "
            "improve clarity, strengthen hooks, and ensure content is publication-ready. "
            "You verify claims are supported by research and optimize for readability."
        ),
        tools=[],
        llm=claude_llm,
        verbose=True,
        allow_delegation=False,
        max_iter=2,
    )
