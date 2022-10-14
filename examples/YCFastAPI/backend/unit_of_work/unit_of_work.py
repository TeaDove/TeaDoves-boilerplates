import ujson
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.base import logger
from core.settings import db_settings

default_args = dict(
    json_deserializer=ujson.loads,
    json_serializer=ujson.dumps,
    pool_size=1,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=60 * 20,
)

_async_engine = create_async_engine(db_settings.dsn, **default_args)
_sessionmaker = sessionmaker(
    _async_engine,
    expire_on_commit=False,
    autocommit=db_settings.autocommit,
    class_=AsyncSession,
)


class AsyncUnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self):
        return self

    async def __aexit__(self, exn_type, _, __):
        if exn_type is not None:
            try:
                logger.debug({"status": "unit.of.work.error"}, exc_info=True)
                await self.rollback()
            except Exception:
                logger.critical({"status": "unable.to.rollback"}, exc_info=True)
        await self.session.close()

    async def begin(self):
        await self.session.begin()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()


class AsyncUnitOfWorkFactory:
    def __call__(self):
        return AsyncUnitOfWork(session=_sessionmaker())
