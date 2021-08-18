"""Configuration for bot instance."""
from botx import Bot, Depends

from app.bot.commands import common, debug, weather
from app.bot.dependencies.crud import auto_models_update
from app.resources import strings
from app.settings.config import get_app_settings

config = get_app_settings()

bot = Bot(
    known_hosts=config.BOT_CREDENTIALS,
    dependencies=[Depends(auto_models_update)],
)

bot.state.bot_name = strings.BOT_NAME

bot.include_collector(common.collector)
bot.include_collector(weather.collector)
bot.include_collector(debug.collector)
