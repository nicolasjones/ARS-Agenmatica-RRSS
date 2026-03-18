from app.agents.services.schedule_service import ScheduleRequest, ScheduleService


class TestScheduleService:
    def test_get_optimal_hours_instagram(self):
        service = ScheduleService()
        hours = service.get_optimal_hours("instagram")
        assert 8 in hours
        assert 19 in hours

    def test_get_optimal_hours_twitter(self):
        service = ScheduleService()
        hours = service.get_optimal_hours("twitter")
        assert len(hours) > 0

    def test_get_optimal_hours_unknown_defaults(self):
        service = ScheduleService()
        hours = service.get_optimal_hours("unknown")
        assert hours == service.get_optimal_hours("twitter")

    def test_suggest_slots_returns_ordered_by_score(self):
        service = ScheduleService()
        request = ScheduleRequest(platform="twitter", content_id="c1")
        slots = service.suggest_slots(request)
        assert len(slots) > 0
        assert slots[0].score >= slots[-1].score

    def test_suggest_slots_excludes_specified_hours(self):
        service = ScheduleService()
        all_hours = service.get_optimal_hours("twitter")
        request = ScheduleRequest(platform="twitter", content_id="c2", exclude_hours=all_hours)
        slots = service.suggest_slots(request)
        assert slots == []

    def test_suggest_slots_platform_in_results(self):
        service = ScheduleService()
        request = ScheduleRequest(platform="linkedin", content_id="c3")
        slots = service.suggest_slots(request)
        assert all(s.platform == "linkedin" for s in slots)
