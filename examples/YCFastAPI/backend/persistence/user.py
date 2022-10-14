from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import UUID

from persistence.base import BaseResource


class User(BaseResource):
    __tablename__ = "user"

    status = Column(Text, nullable=False)
    name = Column(Text, nullable=False)

    auth_id = Column(UUID, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    phone = Column(Text, unique=True, nullable=False)
