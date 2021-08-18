"""App settings for test stage."""
from typing import Any, Optional

from pydantic import Field, PostgresDsn, RedisDsn

from app.settings.environments.base import AppSettings


class TestAppSettings(AppSettings):
    """Application settings with override params for dev environment."""

    # base kwargs
    DEBUG: bool = True
    SQL_DEBUG: bool = True
    BOT_CREDENTIALS: Any = "cts.example.com@secret"

    # storages
    DATABASE_URL: PostgresDsn = Field(
        "postgres://postgres:postgres@localhost/postgres", env="TEST_DB_CONNECTION"
    )
    REDIS_DSN: RedisDsn = "redis://localhost/0"

    # metrics
    SENTRY_DSN: Optional[str] = None

    # db up-time can be more that 25
    RETRY_TIMEOUT: int = 25
    # use local db for tests
    DB: bool = False

    class Config(AppSettings.Config):  # noqa: WPS431
        env_file = ".env"
