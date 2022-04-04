"""Middleware for creating db_session per-request."""

from pybotx_smartapp_rpc import HandlerWithArgs, RPCArgsBaseModel, RPCResponse, SmartApp


async def db_session_middleware(
    smartapp: SmartApp, rpc_arguments: RPCArgsBaseModel, call_next: HandlerWithArgs
) -> RPCResponse:

    session_factory = smartapp.bot.state.db_session_factory

    async with session_factory() as db_session:
        smartapp.state.db_session = db_session

        rpc_response = await call_next(smartapp, rpc_arguments)

        await db_session.commit()

    return rpc_response
