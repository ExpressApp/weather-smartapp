"""Api services."""
from httpx import AsyncClient

from app.schemas.weather import CityResponseSchema, WeatherResponseSchema, WeatherSchema
from app.settings import settings

WEATHER_API_SEARCH = "/search.json"
WEATHER_API_CURRENT_WEATHER = "/current.json"


class WeatherAPIClient:
    def __init__(self) -> None:
        self._async_client = AsyncClient(base_url=settings.WEATHER_API_URL)

    async def get_weather(self, city: str) -> WeatherSchema:
        async with self._async_client as client:
            response = await client.get(
                url=WEATHER_API_CURRENT_WEATHER,
                params={"key": settings.WEATHER_SECRET_KEY, "q": city},
            )
            response.raise_for_status()

        weather_response = WeatherResponseSchema.parse_obj(response.json())
        return weather_response.to_domain()

    async def get_cities(self, city: str) -> CityResponseSchema:
        async with self._async_client as client:
            response = await client.get(
                url=WEATHER_API_SEARCH,
                params={"key": settings.WEATHER_SECRET_KEY, "q": city},
            )
            response.raise_for_status()

        return CityResponseSchema.parse_obj(response.json())


def get_weather_api_client() -> WeatherAPIClient:
    return WeatherAPIClient()
