"""Handlers for default bot commands and system events."""

import asyncio
from uuid import UUID

from botx import Bot, Collector, Message, SendingSmartAppNotification

from app.settings.config import get_app_settings

config = get_app_settings()
collector = Collector()


@collector.hidden(command="/_debug:send_notification_counter")
async def send_notification_counter(
    message: Message,
    bot: Bot,
) -> None:
    smartapp_counter = int(message.command.arguments[0])

    if len(message.command.arguments) > 1:
        group_chat_id = UUID(message.command.arguments[1])
        time_to_sleep = 0
    else:
        group_chat_id = message.group_chat_id
        time_to_sleep = 3

    notification = SendingSmartAppNotification(
        smartapp_counter=smartapp_counter,
        group_chat_id=group_chat_id,
        smartapp_api_version=config.SMARTAPP_API_VERSION,
        opts={},
    )

    await asyncio.sleep(time_to_sleep)
    resp = await bot.send_smartapp_notification(message.credentials, notification)

    await bot.answer_message(
        f"Done.\n{resp}\n{notification.__dict__}", message  # noqa: WPS609
    )
