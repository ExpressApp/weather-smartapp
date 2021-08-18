"""Application with configuration for events, routers and middleware."""
from botx import ServerUnknownError
from fastapi import FastAPI

from app.api.error_handlers import server_unknown
from app.api.routers import router
from app.bot.bot import bot
from app.services.static_files import StaticFilesCustomHeaders
from app.settings.config import get_app_settings
from app.settings.events import shutdown, startup

config = get_app_settings()


def get_application() -> FastAPI:
    """Create configured server application instance."""
    application = FastAPI(title="weatherbot")
    application.state = bot.state
    application.state.bot = bot

    application.add_event_handler(
        "startup",
        startup(
            db_dsn=config.DATABASE_URL,
            bot_app=bot,
        ),
    )

    application.add_event_handler("shutdown", shutdown(bot_app=bot))

    application.add_exception_handler(
        ServerUnknownError, server_unknown.message_from_unknown_server_handler
    )

    application.include_router(router)

    application.mount(
        "/smartapp_files",
        StaticFilesCustomHeaders(
            directory="smartapp_files",
            headers={"cache-control": "max-age=28800, private"},
        ),
        name="smartapp_files",
    )

    return application


app = get_application()
