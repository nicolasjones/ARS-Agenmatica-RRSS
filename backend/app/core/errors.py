from fastapi import HTTPException


class AppError(Exception):
    def __init__(self, message: str, code: str = "INTERNAL_ERROR", status_code: int = 500):
        self.message = message
        self.code = code
        self.status_code = status_code
        super().__init__(message)


class PlatformError(AppError):
    def __init__(self, message: str, platform: str):
        super().__init__(message, code="PLATFORM_ERROR", status_code=502)
        self.platform = platform


class AgentError(AppError):
    def __init__(self, message: str, agent_name: str):
        super().__init__(message, code="AGENT_ERROR", status_code=500)
        self.agent_name = agent_name


class ValidationError(AppError):
    def __init__(self, message: str):
        super().__init__(message, code="VALIDATION_ERROR", status_code=400)


class RateLimitError(AppError):
    def __init__(self, platform: str, retry_after: int | None = None):
        super().__init__(f"Rate limit exceeded for {platform}", code="RATE_LIMIT", status_code=429)
        self.platform = platform
        self.retry_after = retry_after


def app_error_to_http(error: AppError) -> HTTPException:
    return HTTPException(
        status_code=error.status_code,
        detail={"code": error.code, "message": error.message},
    )
