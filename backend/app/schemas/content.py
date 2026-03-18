from datetime import datetime

from pydantic import BaseModel

from app.schemas.common import PlatformType, PostStatus


class ContentCreateRequest(BaseModel):
    topic: str
    platform: PlatformType
    tone: str = "professional"
    brand_voice: str | None = None
    constraints: dict[str, str] | None = None


class ContentResponse(BaseModel):
    id: str
    content: str
    platform: PlatformType
    hashtags: list[str] = []
    media_suggestions: list[str] = []
    status: PostStatus = PostStatus.DRAFT
    created_at: datetime
    updated_at: datetime | None = None


class ContentUpdateRequest(BaseModel):
    content: str | None = None
    hashtags: list[str] | None = None
    status: PostStatus | None = None
