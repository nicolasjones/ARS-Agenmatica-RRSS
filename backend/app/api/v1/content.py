from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter

from app.schemas.common import ApiResponse, PostStatus
from app.schemas.content import ContentCreateRequest, ContentResponse

router = APIRouter()


@router.post("/", response_model=ApiResponse[ContentResponse])
async def create_content(request: ContentCreateRequest) -> ApiResponse[ContentResponse]:
    """Request content generation from ContentCreatorAgent."""
    now = datetime.now(timezone.utc)
    # TODO: Wire to ContentCreatorAgent via CrewAI
    content = ContentResponse(
        id=str(uuid4()),
        content=f"[Generated content for '{request.topic}' on {request.platform}]",
        platform=request.platform,
        hashtags=[],
        media_suggestions=[],
        status=PostStatus.DRAFT,
        created_at=now,
    )
    return ApiResponse(data=content)


@router.get("/", response_model=ApiResponse[list[ContentResponse]])
async def list_content() -> ApiResponse[list[ContentResponse]]:
    """List generated content."""
    # TODO: Wire to database
    return ApiResponse(data=[])
