"""Application with configuration for events, routers and middleware."""

from fastapi import FastAPI

from app.api.routers import router
from app.bot.bot import bot
from app.db.sqlalchemy import build_db_session_factory
from app.resources import strings
from app.services.static_files import StaticFilesCustomHeaders


async def startup() -> None:
    # -- Bot --
    await bot.startup()

    # -- Database --
    bot.state.db_session_factory = await build_db_session_factory()


async def shutdown() -> None:
    # -- Bot --
    await bot.shutdown()


def get_application() -> FastAPI:
    """Create configured server application instance."""

    application = FastAPI(title=strings.BOT_PROJECT_NAME)
    application.state.bot = bot

    application.add_event_handler("startup", startup)
    application.add_event_handler("shutdown", shutdown)

    application.include_router(router)

    application.mount(
        "/smartapp_files",
        StaticFilesCustomHeaders(
            directory="smartapp_files",
            headers={
                "cache-control": "no-store, no-cache, must-revalidate",
                "expires": "-1",
            },
        ),
        name="smartapp_files",
    )

    return application


app = get_application()
