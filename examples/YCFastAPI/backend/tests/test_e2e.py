import asyncio

from unit_of_work.unit_of_work import AsyncUnitOfWorkFactory

unit_of_work_factory = AsyncUnitOfWorkFactory()
loop = asyncio.get_event_loop()


class TestClass:
    async def main(self):
        async with unit_of_work_factory() as uow:
            ...

    def test_ok(self):
        loop.run_until_complete(self.main())
