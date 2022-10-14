from service.service_app import ServiceApp
from unit_of_work.unit_of_work import AsyncUnitOfWorkFactory

service_app = ServiceApp()
unit_of_work_factory = AsyncUnitOfWorkFactory()


class TestClass:
    async def test_process_request(self):
        await service_app.process_request()
