# Platforms Domain

## Overview

Adapters para interactuar con las APIs de cada red social. Cada adapter implementa una interfaz común Python.

## Platform Adapter Interface

```python
class PlatformAdapter(ABC):
    platform: PlatformType

    @abstractmethod
    async def publish(self, post: Post) -> PublishResult: ...

    @abstractmethod
    async def schedule(self, post: Post, publish_at: datetime) -> ScheduleResult: ...

    @abstractmethod
    async def delete_post(self, post_id: str) -> None: ...

    @abstractmethod
    async def get_post_metrics(self, post_id: str) -> PostMetrics: ...

    @abstractmethod
    async def get_account_metrics(self, period: DateRange) -> AccountMetrics: ...

    @abstractmethod
    async def get_comments(self, post_id: str) -> list[Comment]: ...

    @abstractmethod
    async def get_mentions(self, since: datetime) -> list[Mention]: ...
```

## Supported Platforms

| Platform   | API               | Auth       | Key Features              |
|-----------|-------------------|------------|---------------------------|
| Twitter/X | Twitter API v2    | OAuth 2.0  | text, threads, media      |
| Instagram | Meta Graph API    | OAuth 2.0  | posts, stories, reels     |
| LinkedIn  | Marketing API     | OAuth 2.0  | posts, articles           |
| TikTok    | TikTok Dev API    | OAuth 2.0  | video posts, analytics    |

## Content Constraints

| Platform   | Max Text  | Media Types         | Hashtags |
|-----------|-----------|---------------------|----------|
| Twitter/X | 280 chars | img, video, gif     | inline   |
| Instagram | 2200 chars| img, video, carousel| max 30   |
| LinkedIn  | 3000 chars| img, video, doc     | max 5    |
| TikTok    | 2200 chars| video               | inline   |
