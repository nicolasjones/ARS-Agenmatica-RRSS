"""CrewAI orchestration layer — REPLACEABLE.

This module contains CrewAI-specific agent definitions and crew composition.
All business logic lives in app.agents.services.* — these agents are thin wrappers.

To migrate to another orchestrator (e.g., LangGraph):
1. Replace this file with the new orchestrator's agent definitions
2. Keep all services unchanged
3. Wire new agents to the same services
"""

from crewai import Agent, Crew, Process, Task

from app.agents.services.content_service import ContentService
from app.agents.services.schedule_service import ScheduleService
from app.agents.services.analytics_service import AnalyticsService
from app.agents.services.strategy_service import StrategyService


def create_content_agent() -> Agent:
    return Agent(
        role="Content Creator",
        goal="Generate engaging social media content tailored for artists",
        backstory=(
            "You are a creative content strategist specializing in helping artists "
            "build their social media presence. You understand platform-specific "
            "best practices and how to craft authentic content that resonates."
        ),
        verbose=False,
        allow_delegation=False,
    )


def create_scheduler_agent() -> Agent:
    return Agent(
        role="Publishing Scheduler",
        goal="Optimize posting schedules for maximum engagement",
        backstory=(
            "You are a data-driven scheduling expert who analyzes audience patterns "
            "to determine the best times to publish content across platforms."
        ),
        verbose=False,
        allow_delegation=False,
    )


def create_analytics_agent() -> Agent:
    return Agent(
        role="Analytics Analyst",
        goal="Analyze performance metrics and generate actionable insights",
        backstory=(
            "You are a social media analytics expert who transforms raw metrics "
            "into clear, actionable recommendations for artists."
        ),
        verbose=False,
        allow_delegation=False,
    )


def create_strategy_agent() -> Agent:
    return Agent(
        role="Strategy Director",
        goal="Define and optimize content strategy for artist growth",
        backstory=(
            "You are a strategic advisor for creative professionals, combining "
            "market trends, analytics data, and brand identity to craft "
            "effective social media strategies."
        ),
        verbose=False,
        allow_delegation=True,
    )


def build_content_task(agent: Agent, topic: str, platform: str) -> Task:
    service = ContentService()
    from app.agents.services.content_service import ContentBrief

    brief = ContentBrief(topic=topic, platform=platform, tone="authentic")
    prompt = service.build_prompt(brief)

    return Task(
        description=prompt,
        expected_output="A social media post with text, hashtags, and media suggestions",
        agent=agent,
    )


def create_social_crew(topic: str, platform: str) -> Crew:
    """Create a crew for content generation workflow."""
    content_agent = create_content_agent()
    content_task = build_content_task(content_agent, topic, platform)

    return Crew(
        agents=[content_agent],
        tasks=[content_task],
        process=Process.sequential,
        verbose=False,
    )
