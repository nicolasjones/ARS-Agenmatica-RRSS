"""Base platform adapter interface.

All platform adapters must implement this ABC.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Post:
    id: str
    content: str
    platform: str
    media_urls: list[str] | None = None
    hashtags: list[str] | None = None


@dataclass
class PublishResult:
    post_id: str
    platform_post_id: str
    platform: str
    published_at: datetime
    url: str


@dataclass
class PostMetrics:
    post_id: str
    platform: str
    impressions: int
    reach: int
    likes: int
    comments: int
    shares: int
    engagement_rate: float


@dataclass
class DateRange:
    start: datetime
    end: datetime


class PlatformAdapter(ABC):
    """Abstract base for all social media platform adapters."""

    @property
    @abstractmethod
    def platform_name(self) -> str: ...

    @abstractmethod
    async def publish(self, post: Post) -> PublishResult: ...

    @abstractmethod
    async def delete_post(self, post_id: str) -> None: ...

    @abstractmethod
    async def get_post_metrics(self, post_id: str) -> PostMetrics: ...
