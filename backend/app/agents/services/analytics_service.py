"""Analytics service — framework-agnostic business logic.

Handles metrics aggregation and insight generation.
"""

from dataclasses import dataclass


@dataclass
class PostMetricsSummary:
    post_id: str
    platform: str
    impressions: int
    reach: int
    likes: int
    comments: int
    shares: int
    engagement_rate: float


@dataclass
class PlatformInsight:
    platform: str
    total_posts: int
    avg_engagement_rate: float
    best_performing_type: str
    recommendation: str


class AnalyticsService:
    """Framework-agnostic analytics logic."""

    def calculate_engagement_rate(
        self, likes: int, comments: int, shares: int, impressions: int
    ) -> float:
        if impressions == 0:
            return 0.0
        return round(((likes + comments + shares) / impressions) * 100, 2)

    def classify_performance(self, engagement_rate: float) -> str:
        if engagement_rate >= 5.0:
            return "excellent"
        if engagement_rate >= 3.0:
            return "good"
        if engagement_rate >= 1.0:
            return "average"
        return "needs_improvement"

    def generate_insight(self, metrics: list[PostMetricsSummary]) -> PlatformInsight | None:
        if not metrics:
            return None

        platform = metrics[0].platform
        avg_rate = sum(m.engagement_rate for m in metrics) / len(metrics)
        performance = self.classify_performance(avg_rate)

        recommendations = {
            "excellent": "Mantener la estrategia actual, experimentar con nuevos formatos.",
            "good": "Incrementar frecuencia de publicación en horarios pico.",
            "average": "Revisar tipo de contenido y horarios de publicación.",
            "needs_improvement": "Redefinir estrategia de contenido y audiencia objetivo.",
        }

        return PlatformInsight(
            platform=platform,
            total_posts=len(metrics),
            avg_engagement_rate=avg_rate,
            best_performing_type="image",  # placeholder
            recommendation=recommendations[performance],
        )
