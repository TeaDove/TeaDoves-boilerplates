from typing import Callable

from fastapi import Request, Response
from fastapi.routing import APIRoute

from core.base import logger


async def add_event_to_logger(request: Request):
    # Add fastapi context to logs
    fastapi_ctx = {
        "path": request.url.path,
        "method": request.method,
        "body": await request.body(),
        "headers": request.headers,
        "query_params": request.query_params,
    }
    logger.append_keys(fastapi=fastapi_ctx, aws_event=request.scope.get("aws.event"))


class LoggerRouteHandler(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def route_handler(request: Request) -> Response:
            await add_event_to_logger(request)
            logger.debug({"status": "request.received"})
            return await original_route_handler(request)

        return route_handler
