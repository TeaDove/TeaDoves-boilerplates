from datetime import datetime

from presentation.schemas.base import ConfigBaseModel


class GetTimeResponse(ConfigBaseModel):
    timestamp: int
    time: datetime
