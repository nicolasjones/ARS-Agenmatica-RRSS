"""Strategy service — framework-agnostic business logic.

Handles content strategy definition and optimization.
"""

from dataclasses import dataclass, field


@dataclass
class ContentPillar:
    name: str
    description: str
    weight: float  # 0-1, sum of all pillars = 1
    platforms: list[str]


@dataclass
class ContentStrategy:
    artist_name: str
    pillars: list[ContentPillar]
    posting_frequency: dict[str, int]  # platform -> posts per week
    target_audience: str
    brand_voice: str
    goals: list[str] = field(default_factory=list)


class StrategyService:
    """Framework-agnostic strategy logic."""

    def create_default_strategy(self, artist_name: str) -> ContentStrategy:
        return ContentStrategy(
            artist_name=artist_name,
            pillars=[
                ContentPillar(
                    name="Behind the Scenes",
                    description="Creative process, studio, work in progress",
                    weight=0.3,
                    platforms=["instagram", "tiktok"],
                ),
                ContentPillar(
                    name="Finished Work",
                    description="Portfolio pieces, releases, exhibitions",
                    weight=0.3,
                    platforms=["instagram", "twitter", "linkedin"],
                ),
                ContentPillar(
                    name="Community",
                    description="Fan interaction, Q&A, collaborations",
                    weight=0.25,
                    platforms=["twitter", "tiktok"],
                ),
                ContentPillar(
                    name="Education",
                    description="Tips, tutorials, industry insights",
                    weight=0.15,
                    platforms=["linkedin", "tiktok"],
                ),
            ],
            posting_frequency={
                "twitter": 7,
                "instagram": 5,
                "linkedin": 3,
                "tiktok": 4,
            },
            target_audience="Art enthusiasts, collectors, fellow artists",
            brand_voice="Authentic, creative, approachable",
            goals=["Grow audience", "Drive engagement", "Build brand"],
        )

    def validate_pillar_weights(self, pillars: list[ContentPillar]) -> bool:
        total = sum(p.weight for p in pillars)
        return abs(total - 1.0) < 0.01
