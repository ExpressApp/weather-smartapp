"""Functions to create and close connections to db."""

from databases import DatabaseURL
from tortoise import Tortoise


async def init_db(dsn: DatabaseURL) -> None:
    """Create connection to db and init orm models."""
    await Tortoise.init(
        db_url=str(dsn),
        modules={
            "botx": ["app.db.botx.models"],
        },
    )


async def close_db() -> None:
    """Close connection to db."""
    await Tortoise.close_connections()
