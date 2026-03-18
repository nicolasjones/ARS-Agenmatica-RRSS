from app.agents.services.analytics_service import AnalyticsService, PostMetricsSummary


class TestAnalyticsService:
    def test_engagement_rate_normal(self):
        service = AnalyticsService()
        rate = service.calculate_engagement_rate(100, 20, 10, 1000)
        assert rate == 13.0

    def test_engagement_rate_zero_impressions(self):
        service = AnalyticsService()
        rate = service.calculate_engagement_rate(10, 5, 2, 0)
        assert rate == 0.0

    def test_engagement_rate_zero_interactions(self):
        service = AnalyticsService()
        rate = service.calculate_engagement_rate(0, 0, 0, 1000)
        assert rate == 0.0

    def test_engagement_rate_rounding(self):
        service = AnalyticsService()
        rate = service.calculate_engagement_rate(1, 0, 0, 3)
        assert rate == round((1 / 3) * 100, 2)

    def test_classify_performance_excellent(self):
        service = AnalyticsService()
        assert service.classify_performance(6.0) == "excellent"
        assert service.classify_performance(5.0) == "excellent"

    def test_classify_performance_good(self):
        service = AnalyticsService()
        assert service.classify_performance(3.5) == "good"
        assert service.classify_performance(3.0) == "good"

    def test_classify_performance_average(self):
        service = AnalyticsService()
        assert service.classify_performance(1.5) == "average"
        assert service.classify_performance(1.0) == "average"

    def test_classify_performance_needs_improvement(self):
        service = AnalyticsService()
        assert service.classify_performance(0.5) == "needs_improvement"
        assert service.classify_performance(0.0) == "needs_improvement"

    def test_generate_insight_with_metrics(self):
        service = AnalyticsService()
        metrics = [
            PostMetricsSummary("p1", "instagram", 1000, 800, 50, 10, 5, 6.5),
            PostMetricsSummary("p2", "instagram", 1200, 900, 60, 15, 8, 6.9),
        ]
        insight = service.generate_insight(metrics)
        assert insight is not None
        assert insight.platform == "instagram"
        assert insight.total_posts == 2
        assert abs(insight.avg_engagement_rate - (6.5 + 6.9) / 2) < 0.01

    def test_generate_insight_empty_metrics(self):
        service = AnalyticsService()
        insight = service.generate_insight([])
        assert insight is None

    def test_generate_insight_recommendation_present(self):
        service = AnalyticsService()
        metrics = [PostMetricsSummary("p1", "twitter", 500, 300, 5, 1, 0, 0.3)]
        insight = service.generate_insight(metrics)
        assert insight is not None
        assert len(insight.recommendation) > 0


