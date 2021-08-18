"""Base app settings."""
from enum import Enum
from typing import Any, List, Optional

from botx import ExpressServer
from pydantic import BaseSettings, PostgresDsn, RedisDsn, validator, SecretStr


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
    def parse_credentials(cls, credentials: str) -> List[ExpressServer]:  # noqa: N805
        """
        Parse bot credentials separated by comma.

        Each entry must be separated by | or @.
        """
        if not credentials:
            raise ValueError("BotCredentials are required")
        servers = []
        credentials_list = credentials.replace(",", " ").split()
        for server_credentials in credentials_list:
            server_credentials = server_credentials.replace("|", "@")
            host, secret = server_credentials.split("@", 2)
            host, secret = host.strip(), secret.strip()
            servers.append(ExpressServer(host=host, secret_key=secret))

        return servers
