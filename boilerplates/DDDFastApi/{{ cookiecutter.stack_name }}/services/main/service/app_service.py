from datetime import datetime
from typing import Tuple


class AppService:
    @staticmethod
    async def get_time() -> Tuple[datetime, int]:
        return datetime.now(), int(datetime.now().timestamp())
