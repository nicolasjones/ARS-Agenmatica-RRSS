from fastapi import APIRouter

from app.api.v1 import content, health

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(content.router, prefix="/content", tags=["content"])
