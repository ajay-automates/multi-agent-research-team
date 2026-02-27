"""
Multi-Agent Research Team - Task Definitions
Sequential tasks: Research -> Analysis -> Writing -> Editing
"""

from crewai import Task


def create_research_task(agent, topic):
    return Task(
        description=(
            f"Research the following topic thoroughly: {topic}\n\n"
            "Your research must include:\n"
            "1. Search for the latest news and developments (last 7 days preferred)\n"
            "2. Find specific data points, statistics, and facts with sources\n"
            "3. Identify key players, companies, or people involved\n"
            "4. Look for expert opinions and contrarian viewpoints\n"
            "5. Find at least 3-5 credible sources\n\n"
            "Focus on what is NEW and CHANGING, not general background."
        ),
        expected_output=(
            "A comprehensive research brief with: executive summary, "
            "key findings with data points and sources, recent developments with dates, "
            "expert opinions, contrarian perspectives, and list of sources."
        ),
        agent=agent,
    )


def create_analysis_task(agent, topic):
    return Task(
        description=(
            f"Analyze the research findings about: {topic}\n\n"
            "Your analysis must:\n"
            "1. Identify the 3 most important insights from the research\n"
            "2. Find patterns or trends connecting different findings\n"
            "3. Determine what this means for professionals in tech/AI\n"
            "4. Identify the unique angle missing from mainstream coverage\n"
            "5. Rate the significance (1-10) and explain why\n"
            "6. Predict what might happen next"
        ),
        expected_output=(
            "Structured analysis with: 3 key insights ranked by importance, "
            "trend analysis, unique angle, impact assessment, prediction with "
            "confidence level, and significance score 1-10."
        ),
        agent=agent,
    )


def create_writing_task(agent, topic, platforms="linkedin,twitter,newsletter"):
    platform_list = [p.strip().lower() for p in platforms.split(",")]

    instructions = ""
    if "linkedin" in platform_list:
        instructions += (
            "\n\nLINKEDIN POST: Start with a strong hook. 150-300 words. "
            "Use line breaks. Include specific numbers. End with a question. Add 3-5 hashtags."
        )
    if "twitter" in platform_list:
        instructions += (
            "\n\nTWITTER THREAD: Tweet 1 is the hook under 280 chars. "
            "Tweets 2-5 are key insights with data. Final tweet is the takeaway. Number each tweet."
        )
    if "newsletter" in platform_list:
        instructions += (
            "\n\nNEWSLETTER SECTION: Compelling headline. 300-500 word deep-dive. "
            "Context for why this matters NOW. Specific examples. Clear takeaway."
        )

    return Task(
        description=(
            f"Create engaging content about: {topic}\n\n"
            "Using the research and analysis provided, write content for these platforms:"
            f"{instructions}\n\n"
            "RULES: Every claim must be backed by research. Use specific numbers. "
            "Write in first person where appropriate. Make it feel like original insight."
        ),
        expected_output=(
            f"Platform-ready content for: {', '.join(platform_list)}. "
            "Each piece should be complete, formatted, and ready to post."
        ),
        agent=agent,
    )


def create_editing_task(agent, topic):
    return Task(
        description=(
            f"Review and edit all content created about: {topic}\n\n"
            "Your editorial review must:\n"
            "1. FACT CHECK: Verify all claims against the original research\n"
            "2. ACCURACY: Flag any unsupported claims or exaggerations\n"
            "3. ENGAGEMENT: Strengthen hooks, improve readability\n"
            "4. PLATFORM FIT: Ensure each piece follows platform best practices\n"
            "5. CONSISTENCY: Same message across all platforms\n"
            "6. POLISH: Fix grammar, improve word choice, tighten sentences\n\n"
            "Return the FINAL edited versions of all content pieces, clearly labeled."
        ),
        expected_output=(
            "Final edited content for all platforms, each clearly labeled "
            "(LinkedIn / Twitter / Newsletter), fact-checked, hooks strengthened, "
            "platform formatting applied, ready to copy-paste and post."
        ),
        agent=agent,
    )
