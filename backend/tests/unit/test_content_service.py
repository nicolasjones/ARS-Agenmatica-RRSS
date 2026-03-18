from app.agents.services.content_service import ContentBrief, ContentService


class TestContentService:
    def test_get_platform_constraints_twitter(self):
        service = ContentService()
        constraints = service.get_platform_constraints("twitter")
        assert constraints["max_chars"] == 280

    def test_get_platform_constraints_instagram(self):
        service = ContentService()
        constraints = service.get_platform_constraints("instagram")
        assert constraints["max_chars"] == 2200
        assert constraints["max_hashtags"] == 30

    def test_get_platform_constraints_unknown_defaults_to_twitter(self):
        service = ContentService()
        constraints = service.get_platform_constraints("unknown_platform")
        assert constraints["max_chars"] == 280

    def test_build_prompt_includes_topic_and_platform(self):
        service = ContentService()
        brief = ContentBrief(topic="art show", platform="instagram", tone="creative")
        prompt = service.build_prompt(brief)
        assert "instagram" in prompt
        assert "art show" in prompt
        assert "2200" in prompt

    def test_build_prompt_includes_brand_voice(self):
        service = ContentService()
        brief = ContentBrief(topic="concert", platform="twitter", tone="exciting", brand_voice="edgy and bold")
        prompt = service.build_prompt(brief)
        assert "edgy and bold" in prompt

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

    def test_validate_content_exactly_at_limit(self):
        service = ContentService()
        text_at_limit = "x" * 280
        issues = service.validate_content(text_at_limit, "twitter")
        assert issues == []

    def test_extract_hashtags(self):
        service = ContentService()
        tags = service.extract_hashtags("Check out my #art #gallery today")
        assert tags == ["#art", "#gallery"]

    def test_extract_hashtags_empty(self):
        service = ContentService()
        tags = service.extract_hashtags("No hashtags here")
        assert tags == []
