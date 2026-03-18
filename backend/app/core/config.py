from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ARS Agenmatica RRSS"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"

    # Database
    database_url: str = "postgresql://user:password@localhost:5432/ars_agenmatica"

    # Redis
    redis_url: str = "redis://localhost:6379"

    # AI / LLM
    anthropic_api_key: str = ""
    openai_api_key: str = ""

    # Platform credentials
    twitter_api_key: str = ""
    twitter_api_secret: str = ""
    twitter_access_token: str = ""

    meta_app_id: str = ""
    meta_app_secret: str = ""
    instagram_access_token: str = ""

    linkedin_client_id: str = ""
    linkedin_client_secret: str = ""

    tiktok_client_key: str = ""
    tiktok_client_secret: str = ""

    # Logging
    log_level: str = "info"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
