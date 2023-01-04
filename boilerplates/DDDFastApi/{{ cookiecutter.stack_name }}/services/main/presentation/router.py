from fastapi import APIRouter, Depends

from presentation.dependencies import get_app_service
from presentation.logs_utils import LoggerRouteHandler
from presentation.schemas.time import GetTimeResponse
from service.app_service import AppService
from shared.base import logger

router = APIRouter(prefix="", route_class=LoggerRouteHandler)


@router.get("/now", response_model=GetTimeResponse)
async def get_region_config(app_service: AppService = Depends(get_app_service)):
    now = app_service.get_time()
    logger.debug({"status": "debug.log"})
    logger.info(now)
    return GetTimeResponse(timestamp=now[1], time=now[0])
