from app.agents.services.strategy_service import ContentPillar, StrategyService


class TestStrategyService:
    def test_create_default_strategy_artist_name(self):
        service = StrategyService()
        strategy = service.create_default_strategy("Test Artist")
        assert strategy.artist_name == "Test Artist"

    def test_create_default_strategy_has_four_pillars(self):
        service = StrategyService()
        strategy = service.create_default_strategy("Test Artist")
        assert len(strategy.pillars) == 4

    def test_create_default_strategy_pillar_weights_sum_to_one(self):
        service = StrategyService()
        strategy = service.create_default_strategy("Test Artist")
        assert service.validate_pillar_weights(strategy.pillars)

    def test_create_default_strategy_has_posting_frequency(self):
        service = StrategyService()
        strategy = service.create_default_strategy("Test Artist")
        assert "twitter" in strategy.posting_frequency
        assert "instagram" in strategy.posting_frequency
        assert all(v > 0 for v in strategy.posting_frequency.values())

    def test_create_default_strategy_has_goals(self):
        service = StrategyService()
        strategy = service.create_default_strategy("Test Artist")
        assert len(strategy.goals) > 0

    def test_validate_pillar_weights_valid(self):
        service = StrategyService()
        pillars = [
            ContentPillar("a", "desc", 0.5, ["twitter"]),
            ContentPillar("b", "desc", 0.5, ["instagram"]),
        ]
        assert service.validate_pillar_weights(pillars)

    def test_validate_pillar_weights_invalid_sum(self):
        service = StrategyService()
        pillars = [ContentPillar("a", "desc", 0.5, ["twitter"])]
        assert not service.validate_pillar_weights(pillars)

    def test_validate_pillar_weights_over_one(self):
        service = StrategyService()
        pillars = [
            ContentPillar("a", "desc", 0.7, ["twitter"]),
            ContentPillar("b", "desc", 0.7, ["instagram"]),
        ]
        assert not service.validate_pillar_weights(pillars)

    def test_validate_pillar_weights_empty(self):
        service = StrategyService()
        assert not service.validate_pillar_weights([])
