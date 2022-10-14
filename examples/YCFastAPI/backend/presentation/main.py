from fastapi import FastAPI, Request, status
from fastapi.responses import UJSONResponse
from starlette.exceptions import ExceptionMiddleware

from core.base import logger
from core.settings import app_settings
from presentation.routers import router_app


def create_app() -> FastAPI:
    fastapi_app = FastAPI(
        docs_url="/docs" if app_settings.show_swagger else None,
        redoc_url="/redoc" if app_settings.show_swagger else None,
        openapi_url="/openapi.json" if app_settings.show_swagger else None,
    )
    fastapi_app.add_middleware(ExceptionMiddleware, handlers=fastapi_app.exception_handlers)
    fastapi_app.include_router(router_app.router)
    return fastapi_app


app = create_app()


@app.exception_handler(Exception)
async def unhandled_exception_handler(_: Request, __: Exception):
    logger.critical({"status": "internal.server.error"}, exc_info=True)
    return UJSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "internal.server.error"})
