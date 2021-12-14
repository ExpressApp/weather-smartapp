"""Base app settings."""
from enum import Enum
from typing import Any, List, Optional

from botx import BotXCredentials
from pydantic import BaseSettings, PostgresDsn, RedisDsn, SecretStr, validator


class AppEnvTypes(str, Enum):  # noqa:WPS600, WPS115
    """Types of stages."""

    PROD: str = "prod"
    DEV: str = "dev"
    TEST: str = "test"


class BaseAppSettings(BaseSettings):
    """Allows to determine the current application environment."""

    APP_ENV: AppEnvTypes = AppEnvTypes.DEV

    class Config:  # noqa: WPS431
        env_file = ".env"


class AppSettings(BaseAppSettings):
    """Main settings for splitting."""

    class Config:  # noqa: WPS431
        env_file = ".env"

    # base kwargs
    DEBUG: bool
    SQL_DEBUG: bool
    BOT_CREDENTIALS: Any

    # storages
    DATABASE_URL: PostgresDsn
    REDIS_DSN: RedisDsn

    # metrics
    SENTRY_DSN: Optional[str] = None

    SMARTAPP_API_VERSION: int
    WEATHER_SECRET_KEY: SecretStr

    @validator("BOT_CREDENTIALS", pre=True)
    @classmethod
    def parse_bot_credentials(cls, raw_credentials: Any) -> List[BotXCredentials]:
        """Parse bot credentials separated by comma.

        Each entry must be separated by "@".
        """
        if not raw_credentials:
            raise ValueError("`BOT_CREDENTIALS` can't be empty")

        return [
            cls._build_credentials_from_string(credentials_str)
            for credentials_str in raw_credentials.replace(",", " ").split()
        ]

    @classmethod
    def _build_credentials_from_string(cls, credentials_str: str) -> BotXCredentials:
        credentials_str = credentials_str.replace("|", "@")
        assert (  # noqa: S101
            credentials_str.count("@") == 2
        ), "Have you forgot to add `bot_id`?"

        host, secret_key, bot_id = [
            str_value.strip() for str_value in credentials_str.split("@")
        ]
        return BotXCredentials(host=host, secret_key=secret_key, bot_id=bot_id)
