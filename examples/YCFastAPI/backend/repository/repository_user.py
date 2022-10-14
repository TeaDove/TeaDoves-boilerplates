import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from persistence.user import User


class RepositoryUser:
    @staticmethod
    async def get_user_by_auth_id(db_session: AsyncSession, auth_id: uuid.UUID) -> User:
        statement = select(User).where(User.auth_id == str(auth_id))
        result = await db_session.execute(statement)
        return result.scalar()
