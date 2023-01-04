from datetime import datetime
from typing import Tuple


class AppService:
    def get_time(self) -> Tuple[datetime, int]:
        return datetime.now(), int(datetime.now().timestamp())
