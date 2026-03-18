"""Schedule service — framework-agnostic business logic.

Handles publishing schedule optimization independent of any orchestrator.
"""

from dataclasses import dataclass, field
from datetime import datetime

# Optimal posting hours by platform (UTC) based on general engagement data
OPTIMAL_HOURS: dict[str, list[int]] = {
    "twitter": [9, 12, 15, 18],
    "instagram": [8, 11, 14, 19],
    "linkedin": [8, 10, 12, 17],
    "tiktok": [10, 14, 19, 21],
}


@dataclass
class ScheduleSlot:
    platform: str
    suggested_time: datetime
    score: float  # 0-1 confidence score
    reason: str


@dataclass
class ScheduleRequest:
    platform: str
    content_id: str
    preferred_date: datetime | None = None
    timezone: str = "UTC"
    exclude_hours: list[int] = field(default_factory=list)


class ScheduleService:
    """Framework-agnostic scheduling logic."""

    def get_optimal_hours(self, platform: str) -> list[int]:
        return OPTIMAL_HOURS.get(platform, OPTIMAL_HOURS["twitter"])

    def suggest_slots(self, request: ScheduleRequest) -> list[ScheduleSlot]:
        """Suggest optimal time slots for publishing."""
        optimal = self.get_optimal_hours(request.platform)
        available = [h for h in optimal if h not in request.exclude_hours]

        slots: list[ScheduleSlot] = []
        for i, hour in enumerate(available):
            score = 1.0 - (i * 0.15)  # First slot gets highest score
            slots.append(
                ScheduleSlot(
                    platform=request.platform,
                    suggested_time=datetime(2024, 1, 1, hour, 0),  # placeholder date
                    score=max(score, 0.3),
                    reason=f"Peak engagement hour for {request.platform}",
                )
            )
        return slots
