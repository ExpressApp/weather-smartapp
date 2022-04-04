"""Domains user."""
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.db.weather.models import UserModel


class User(BaseModel):
    user_huid: UUID
    city: Optional[str] = None

    @classmethod
    async def from_orm(cls, user: UserModel) -> "User":
        return cls(user_huid=user.user_huid, city=user.city)
