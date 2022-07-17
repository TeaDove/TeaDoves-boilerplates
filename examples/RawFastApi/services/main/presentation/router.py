from datetime import datetime

from fastapi import APIRouter

from core.base import logger
from presentation.schemas.time import GetTimeResponse

router = APIRouter(prefix="")


@router.get("/now", response_model=GetTimeResponse)
async def get_region_config():
    logger.info({"status": "got.request!"})
    now = datetime.now(), int(datetime.now().timestamp())
    return GetTimeResponse(timestamp=now[1], time=now[0])
