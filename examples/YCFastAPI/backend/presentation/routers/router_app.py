from fastapi import APIRouter, Depends, Request

from presentation.auth_utils import get_yc_token
from presentation.dependencies import get_service_app
from presentation.logs_utils import LoggerRouteHandler
from service.service_app import ServiceApp

router = APIRouter(prefix="", route_class=LoggerRouteHandler)


@router.get("/")
async def hello_world(service_app: ServiceApp = Depends(get_service_app), _: str = Depends(get_yc_token)) -> str:
    return await service_app.process_request()


@router.get("/ip")
def get_ip(request: Request) -> str:
    return request.client.host
