import pytest
from pydantic import ValidationError

from app.settings.environments.test import AppSettings


def test_credentions_validation():
    AppSettings(
        DEBUG=True,
        SQL_DEBUG=True,
        BOT_CREDENTIALS="any@secret",
        SENTRY_DSN=None,
    )
    with pytest.raises(ValidationError):
        AppSettings(
            DEBUG=True,
            SQL_DEBUG=True,
            BOT_CREDENTIALS=None,
            SENTRY_DSN=None,
        )
