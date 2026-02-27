"""
Multi-Agent Research Team - Crew Orchestration
Research -> Analysis -> Writing -> Editing
"""

from crewai import Crew, Process
import time

from agents import create_researcher, create_analyst, create_writer, create_editor
from tasks import create_research_task, create_analysis_task, create_writing_task, create_editing_task


class ResearchCrew:
    """Orchestrates the multi-agent research team."""

    def __init__(self):
        self.researcher = create_researcher()
        self.analyst = create_analyst()
        self.writer = create_writer()
        self.editor = create_editor()

    def run(self, topic, platforms="linkedin,twitter,newsletter"):
        start_time = time.time()

        research_task = create_research_task(self.researcher, topic)
        analysis_task = create_analysis_task(self.analyst, topic)
        writing_task = create_writing_task(self.writer, topic, platforms)
        editing_task = create_editing_task(self.editor, topic)

        crew = Crew(
            agents=[self.researcher, self.analyst, self.writer, self.editor],
            tasks=[research_task, analysis_task, writing_task, editing_task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        elapsed = round(time.time() - start_time, 2)

        return {
            "topic": topic,
            "platforms": platforms,
            "final_output": str(result),
            "task_outputs": [
                {"agent": "Researcher", "task": "Research", "output": str(research_task.output) if research_task.output else "N/A"},
                {"agent": "Analyst", "task": "Analysis", "output": str(analysis_task.output) if analysis_task.output else "N/A"},
                {"agent": "Writer", "task": "Writing", "output": str(writing_task.output) if writing_task.output else "N/A"},
                {"agent": "Editor", "task": "Editing", "output": str(editing_task.output) if editing_task.output else "N/A"},
            ],
            "metrics": {
                "total_agents": 4,
                "total_tasks": 4,
                "process": "sequential",
                "latency_seconds": elapsed,
            }
        }


if __name__ == "__main__":
    import sys
    topic = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Latest developments in AI agents"
    print(f"Starting Research Crew on: {topic}")
    crew = ResearchCrew()
    result = crew.run(topic)
    print("=" * 80)
    print("FINAL OUTPUT")
    print("=" * 80)
    print(result["final_output"])
    print(f"Completed in {result['metrics']['latency_seconds']}s with {result['metrics']['total_agents']} agents")
