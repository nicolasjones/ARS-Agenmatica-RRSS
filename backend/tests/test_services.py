"""Tests for framework-agnostic business services."""

from app.agents.services.content_service import ContentBrief, ContentService
from app.agents.services.schedule_service import ScheduleRequest, ScheduleService
from app.agents.services.analytics_service import AnalyticsService, PostMetricsSummary
from app.agents.services.strategy_service import StrategyService


class TestContentService:
    def test_get_platform_constraints(self):
        service = ContentService()
        constraints = service.get_platform_constraints("twitter")
        assert constraints["max_chars"] == 280

    def test_build_prompt(self):
        service = ContentService()
        brief = ContentBrief(topic="art show", platform="instagram", tone="creative")
        prompt = service.build_prompt(brief)
        assert "instagram" in prompt
        assert "art show" in prompt
        assert "2200" in prompt

    def test_validate_content_ok(self):
        service = ContentService()
        issues = service.validate_content("Short post", "twitter")
        assert issues == []

    def test_validate_content_too_long(self):
        service = ContentService()
        long_text = "x" * 300
        issues = service.validate_content(long_text, "twitter")
        assert len(issues) == 1
        assert "280" in issues[0]

    def test_extract_hashtags(self):
        service = ContentService()
        tags = service.extract_hashtags("Check out my #art #gallery today")
        assert tags == ["#art", "#gallery"]


class TestScheduleService:
    def test_get_optimal_hours(self):
        service = ScheduleService()
        hours = service.get_optimal_hours("instagram")
        assert 8 in hours
        assert 19 in hours

    def test_suggest_slots(self):
        service = ScheduleService()
        request = ScheduleRequest(platform="twitter", content_id="c1")
        slots = service.suggest_slots(request)
        assert len(slots) > 0
        assert slots[0].score >= slots[-1].score


class TestAnalyticsService:
    def test_engagement_rate(self):
        service = AnalyticsService()
        rate = service.calculate_engagement_rate(100, 20, 10, 1000)
        assert rate == 13.0

    def test_engagement_rate_zero_impressions(self):
        service = AnalyticsService()
        rate = service.calculate_engagement_rate(10, 5, 2, 0)
        assert rate == 0.0

    def test_classify_performance(self):
        service = AnalyticsService()
        assert service.classify_performance(6.0) == "excellent"
        assert service.classify_performance(3.5) == "good"
        assert service.classify_performance(1.5) == "average"
        assert service.classify_performance(0.5) == "needs_improvement"

    def test_generate_insight(self):
        service = AnalyticsService()
        metrics = [
            PostMetricsSummary("p1", "instagram", 1000, 800, 50, 10, 5, 6.5),
            PostMetricsSummary("p2", "instagram", 1200, 900, 60, 15, 8, 6.9),
        ]
        insight = service.generate_insight(metrics)
        assert insight is not None
        assert insight.platform == "instagram"
        assert insight.total_posts == 2


class TestStrategyService:
    def test_create_default_strategy(self):
        service = StrategyService()
        strategy = service.create_default_strategy("Test Artist")
        assert strategy.artist_name == "Test Artist"
        assert len(strategy.pillars) == 4
        assert service.validate_pillar_weights(strategy.pillars)

    def test_validate_pillar_weights_invalid(self):
        service = StrategyService()
        from app.agents.services.strategy_service import ContentPillar

        bad_pillars = [ContentPillar("a", "a", 0.5, ["twitter"])]
        assert not service.validate_pillar_weights(bad_pillars)
