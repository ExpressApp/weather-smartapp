"""Repository for weather user models."""
from uuid import UUID

from app.db.crud import CRUD
from app.db.sqlalchemy import AsyncSession
from app.db.weather.models import UserModel
from app.schemas.user import User


class UserRepo:
    def __init__(self, session: AsyncSession):
        """Initialize repo with CRUD."""
        self._crud = CRUD(session=session, cls_model=UserModel)

    async def get_user_by_huid(self, user_huid: UUID) -> User:
        """Get user by huid."""
        row = await self._crud.get_or_none(pkey_val=user_huid)
        if row:
            return await User.from_orm(row)

        row = await self._crud.create(model_data={"user_huid": user_huid})
        user_in_db = await self._crud.get(pkey_val=row.user_huid)
        return await User.from_orm(user_in_db)

    async def update_user_city(self, user_huid: UUID, city: str) -> None:
        """Update the weather in the user's city."""
        await self._crud.update(pkey_val=user_huid, model_data={"city": city})
