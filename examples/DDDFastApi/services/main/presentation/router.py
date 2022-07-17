from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from core.containers import ApplicationContainer
from presentation.logs_utils import LoggerRouteHandler
from presentation.schemas.time import GetTimeResponse
from service.app_service import AppService

router = APIRouter(prefix="", route_class=LoggerRouteHandler)


@router.get("/now", response_model=GetTimeResponse)
@inject
async def get_region_config(app_service: AppService = Depends(Provide[ApplicationContainer.services.app_service])):
    now = await app_service.get_time()
    return GetTimeResponse(timestamp=now[1], time=now[0])
