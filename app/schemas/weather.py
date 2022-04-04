"""Domains weather."""
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, validator


class WeatherSchema(BaseModel):
    city: str
    weather: Dict[str, Any]


class WeatherResponseSchema(BaseModel):
    location: Union[Dict[str, Any], Any]
    current: Dict[str, Any]

    @validator("location", pre=True)
    def parse_location(cls, location: dict) -> Optional[str]:  # noqa: N805
        return location.get("name")

    def to_domain(self) -> WeatherSchema:
        return WeatherSchema(city=self.location, weather=self.current)


class CitySchema(BaseModel):
    country: str
    name: str
    region: str


class CityResponseSchema(BaseModel):
    __root__: List[CitySchema]
