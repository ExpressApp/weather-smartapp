"""Definition for error handler for message from unregistered CTS."""

from botx import BotDisabledErrorData, BotDisabledResponse, ServerUnknownError
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE


async def message_from_unknown_server_handler(
    _request: Request, exc: ServerUnknownError
) -> Response:
    """Handle error for message from unknown CTS."""
    return JSONResponse(
        status_code=HTTP_503_SERVICE_UNAVAILABLE,
        content=BotDisabledResponse(
            error_data=BotDisabledErrorData(
                status_message=(
                    f"Sorry, bot can not communicate with users from {exc.host} CTS"
                )
            )
        ).dict(),
    )
