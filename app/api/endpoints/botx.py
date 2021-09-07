"""Endpoints for communication with botx."""

from botx import IncomingMessage, Message, SendingSmartApp, Status
from botx.clients.methods.v3.smartapp import post as smartapp_method
from botx.models import events
from botx.models.status import StatusRecipient
from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.status import HTTP_202_ACCEPTED

from app.api.dependencies.status_recipient import get_status_recipient
from app.bot.bot import bot
from app.bot.commands.weather import execute_smart_app

router = APIRouter()


@router.post("/command", name="botx:command", status_code=HTTP_202_ACCEPTED)
async def bot_command(message: IncomingMessage) -> None:
    """Receive commands from users. Max timeout - 5 seconds."""

    await bot.execute_command(message.dict())


@router.get("/status", name="botx:status", response_model=Status)
async def bot_status(
    recipient: StatusRecipient = Depends(get_status_recipient),
) -> Status:
    """Send commands with short descriptions."""
    return await bot.status()


@router.post(
    "/command/smartapp", name="debug:samrtapp-event", status_code=HTTP_202_ACCEPTED
)
async def smartapp_debug(message: IncomingMessage) -> dict:
    """Send botx command to sender."""
    # all internal mutations
    bot_message = Message.from_dict(message.dict(), bot)
    incoming_smartapp = events.SmartAppEvent(
        **bot_message.data.__dict__  # noqa: WPS609
    )

    try:
        response = await execute_smart_app(incoming_smartapp)
    except Exception as exc:
        return {"executing command error": exc.args}

    sending_smartapp = SendingSmartApp.from_message_with_smartapp(response, bot_message)

    sending_smartapp_dict = smartapp_method.SmartAppEvent(
        **sending_smartapp.dict()
    ).dict()
    return {**sending_smartapp_dict}


@router.post("/command/echo", name="debug:echo", status_code=HTTP_202_ACCEPTED)
async def smartapp_echo(request: Request) -> dict:
    """Echo."""

    return await request.json()
