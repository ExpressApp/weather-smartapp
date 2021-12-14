"""Handlers for default bot commands and system events."""
import pprint
from typing import Any

import httpx
from botx import Collector, Message, SendingSmartAppEvent
from botx.models.events import SmartAppEvent
from loguru import logger

from app.db.botx.repo import get_user_by_huid
from app.settings.config import get_app_settings

collector = Collector()

DEBUG_USERS = set()
ECHO = False


GET_CITIES_SMARTAPP_TYPE = "cities_autocomplete"
GET_CURRENT_WEATHER_SMARAPP_TYPE = "current_weather"
GET_INITIAL_WEATHER_SMARTAPP_TYPE = "initial_state"

WEATHER_API_BASE_URL = "https://api.weatherapi.com/v1"
WEATHER_API_SEARCH = "/search.json"
WEATHER_API_CURRENT_WHEATHER = "/current.json"


@collector.hidden(command="/debug")
async def show_all_messages(message: Message) -> None:
    if message.user_huid not in DEBUG_USERS:
        DEBUG_USERS.add(message.user_huid)
    else:
        DEBUG_USERS.remove(message.user_huid)


async def get_weather(endpoint: str, query: dict) -> dict:
    client: httpx.AsyncClient
    async with httpx.AsyncClient(base_url=WEATHER_API_BASE_URL) as client:
        config = get_app_settings()
        response = await client.get(
            endpoint,
            params={"key": config.WEATHER_SECRET_KEY.get_secret_value(), **query},
        )
        response.raise_for_status()
        logger.info(response.request.url)
        return response.json()


async def execute_smart_app(message: Message) -> Any:  # noqa: WPS231
    smartapp = SmartAppEvent(**message.data)  # noqa: WPS609

    smartapp_type = smartapp.data["type"]
    response = {"type": smartapp_type}
    if smartapp_type == GET_CITIES_SMARTAPP_TYPE:
        all_cities = await get_weather(
            WEATHER_API_SEARCH, {"q": smartapp.data["query"]}
        )
        response.update({"cities": all_cities})
    elif smartapp_type == GET_CURRENT_WEATHER_SMARAPP_TYPE:

        user = await get_user_by_huid(message.user_huid)
        user.last_city_request = smartapp.data["query"]
        await user.save()

        current_weather = await get_weather(
            WEATHER_API_CURRENT_WHEATHER,
            {"q": smartapp.data["query"], "aqi": "no"},
        )
        current_weather.pop("location")
        current_weather["weather"] = current_weather.pop("current")
        current_weather["city"] = smartapp.data["query"]
        response.update(current_weather)
    elif smartapp_type == GET_INITIAL_WEATHER_SMARTAPP_TYPE:
        city = (await get_user_by_huid(message.user_huid)).last_city_request

        current_weather = {}
        if city:
            current_weather = await get_weather(
                WEATHER_API_CURRENT_WHEATHER,
                {"q": city, "aqi": "no"},
            )
            current_weather.pop("location")
            current_weather["weather"] = current_weather.pop("current")

        current_weather["city"] = city
        response.update(current_weather)
    else:
        raise ValueError
    return response


@collector.smartapp_event()
async def smartapp_handler(message: Message) -> None:
    # get smartapp.
    incoming_smartapp = SmartAppEvent(**message.data)  # noqa: WPS609

    response = await execute_smart_app(message)

    # helper for construct sending data.
    sending_smartapp = SendingSmartAppEvent.from_message(response, message)

    await message.bot.send_smartapp_event(message.credentials, sending_smartapp)

    # logging
    incoming_log = f"incoming message:\n{pprint.pformat(incoming_smartapp.dict())}"
    outgoing_log = f"outgoing message:\n{pprint.pformat(sending_smartapp.dict())}"
    logger.info(incoming_log)
    logger.info(outgoing_log)

    # debug
    if message.user_huid in DEBUG_USERS:
        await message.bot.answer_message(incoming_log, message)
        await message.bot.answer_message(outgoing_log, message)
