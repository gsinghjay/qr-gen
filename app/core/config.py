"""Application configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    PROJECT_NAME: str = "QR Code Generator"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    # Database settings
    DATABASE_URL: str = "sqlite:///./test.db"

    class Config:
        """Pydantic config."""

        case_sensitive = True
        env_file = ".env"


settings = Settings()
