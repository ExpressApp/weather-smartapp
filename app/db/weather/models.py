"""Main models for storing bot data."""

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.sqlalchemy import Base


class UserModel(Base):
    """User database."""

    __tablename__ = "user"

    user_huid = Column(UUID(as_uuid=True), primary_key=True)
    city = Column(String(), nullable=True)
