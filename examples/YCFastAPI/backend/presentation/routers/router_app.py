from fastapi import APIRouter, Depends, Request

from presentation.auth_utils import get_yc_token
from presentation.logs_utils import LoggerRouteHandler

router = APIRouter(prefix="", route_class=LoggerRouteHandler)


@router.get("/")
async def hello_world(request: Request, _: str = Depends(get_yc_token)) -> str:
    return await request.app.service_app.process_request()


@router.get("/ip")
def get_ip(request: Request) -> str:
    return request.client.host
