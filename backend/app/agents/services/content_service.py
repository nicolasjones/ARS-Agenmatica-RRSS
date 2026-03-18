"""Content generation service — framework-agnostic business logic.

This service contains all content creation rules and logic.
It has NO dependency on CrewAI or any orchestrator.
"""

from dataclasses import dataclass

PLATFORM_CONSTRAINTS: dict[str, dict[str, int | list[str]]] = {
    "twitter": {"max_chars": 280, "max_hashtags": 5, "media_types": ["image", "video", "gif"]},
    "instagram": {"max_chars": 2200, "max_hashtags": 30, "media_types": ["image", "video", "carousel"]},
    "linkedin": {"max_chars": 3000, "max_hashtags": 5, "media_types": ["image", "video", "document"]},
    "tiktok": {"max_chars": 2200, "max_hashtags": 10, "media_types": ["video"]},
}


@dataclass
class ContentBrief:
    topic: str
    platform: str
    tone: str
    brand_voice: str | None = None
    constraints: dict[str, str] | None = None


@dataclass
class GeneratedContent:
    text: str
    hashtags: list[str]
    media_suggestions: list[str]
    platform: str
    character_count: int


class ContentService:
    """Framework-agnostic content generation logic."""

    def get_platform_constraints(self, platform: str) -> dict[str, int | list[str]]:
        return PLATFORM_CONSTRAINTS.get(platform, PLATFORM_CONSTRAINTS["twitter"])

    def build_prompt(self, brief: ContentBrief) -> str:
        constraints = self.get_platform_constraints(brief.platform)
        max_chars = constraints["max_chars"]

        prompt = (
            f"Create a social media post for {brief.platform} about: {brief.topic}\n"
            f"Tone: {brief.tone}\n"
            f"Max characters: {max_chars}\n"
        )

        if brief.brand_voice:
            prompt += f"Brand voice: {brief.brand_voice}\n"

        prompt += (
            "\nReturn the post text, relevant hashtags, and media suggestions.\n"
            "The content should be optimized for artist/creative audiences."
        )
        return prompt

    def validate_content(self, content: str, platform: str) -> list[str]:
        """Validate content against platform constraints. Returns list of issues."""
        constraints = self.get_platform_constraints(platform)
        issues: list[str] = []
        max_chars = constraints["max_chars"]

        if isinstance(max_chars, int) and len(content) > max_chars:
            issues.append(f"Content exceeds {max_chars} character limit ({len(content)} chars)")

        return issues

    def extract_hashtags(self, text: str) -> list[str]:
        """Extract hashtags from text."""
        return [word for word in text.split() if word.startswith("#")]
