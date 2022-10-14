import uuid

from sqlalchemy import BigInteger, Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import func

Base = declarative_base()
metadata = Base.metadata


class BaseModel(Base):
    __abstract__ = True
    __table_args__ = {"schema": "public"}


class BaseEntity(Base):
    __abstract__ = True
    __table_args__ = {"schema": "public"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)


class BaseResource(Base):
    __abstract__ = True
    __table_args__ = {"schema": "public"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    external_id = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now(), index=True)
    modified_at = Column(DateTime(timezone=True), onupdate=func.now(), index=True)
