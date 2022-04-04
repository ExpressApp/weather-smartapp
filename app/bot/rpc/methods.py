"""RPC methods."""
from pybotx_smartapp_rpc import RPCArgsBaseModel, RPCResultResponse, RPCRouter, SmartApp

from app.bot.middlewares.db_session import db_session_middleware
from app.db.weather.repo import UserRepo
from app.schemas.weather import WeatherSchema
from app.services.weather_api import get_weather_api_client

rpc = RPCRouter()


class WeatherQuery(RPCArgsBaseModel):
    city: str


@rpc.method("cities_autocomplete")
async def cities_autocomplete(
    smartapp: SmartApp,
    query: WeatherQuery,
) -> RPCResultResponse[WeatherSchema]:
    weather_client = get_weather_api_client()
    response = {"cities": await weather_client.get_cities(query.city)}

    return RPCResultResponse(result=response)


@rpc.method("current_weather", middlewares=[db_session_middleware])
async def current_weather(
    smartapp: SmartApp,
    query: WeatherQuery,
) -> RPCResultResponse[WeatherSchema]:
    weather_client = get_weather_api_client()
    user_repo = UserRepo(smartapp.state.db_session)

    user = await user_repo.get_user_by_huid(user_huid=smartapp.event.sender.huid)

    if user.city != query.city:
        await user_repo.update_user_city(user.user_huid, query.city)

    weather = await weather_client.get_weather(query.city)
    return RPCResultResponse(result=weather)


@rpc.method("initial_state", middlewares=[db_session_middleware])
async def initial_state(
    smartapp: SmartApp,
) -> RPCResultResponse[WeatherSchema]:
    weather_client = get_weather_api_client()
    user_repo = UserRepo(smartapp.state.db_session)

    city = (await user_repo.get_user_by_huid(smartapp.event.sender.huid)).city
    if city:
        weather = await weather_client.get_weather(city)

        return RPCResultResponse(result=weather)

    return RPCResultResponse(result={"city": None})
