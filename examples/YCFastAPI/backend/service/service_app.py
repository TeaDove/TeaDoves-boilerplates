from core.base import logger


class ServiceApp:
    async def process_request(self):
        logger.info({"status": "ok"})
        return "ok"
