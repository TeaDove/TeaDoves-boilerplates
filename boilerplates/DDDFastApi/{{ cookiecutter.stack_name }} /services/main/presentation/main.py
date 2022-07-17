from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError, StarletteHTTPException
from fastapi.responses import UJSONResponse
from starlette.exceptions import ExceptionMiddleware

from core.base import logger
from core.containers import ApplicationContainer
from core.settings import app_settings
from presentation.router import router


def create_app() -> FastAPI:
    fastapi_app = FastAPI(
        docs_url=None if app_settings.show_swagger else "/docs",
        redoc_url=None if app_settings.show_swagger else "/redoc",
        openapi_url=None if app_settings.show_swagger else "/openapi.json",
    )
    fastapi_app.add_middleware(ExceptionMiddleware, handlers=fastapi_app.exception_handlers)
    fastapi_app.include_router(router)
    container = ApplicationContainer()
    fastapi_app.container = container
    return fastapi_app


app = create_app()


@app.exception_handler(StarletteHTTPException)
async def starlette_generic_exception_handler(_: Request, __: StarletteHTTPException):
    logger.warning({"status": "bad.request.error"}, exc_info=True)
    return UJSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": {"code": "bad.request", "message": "Bad request"}},
    )


@app.exception_handler(RequestValidationError)
async def request_validation_error_handler(_: Request, exc: RequestValidationError):
    logger.warning({"status": "request.validation.error"}, exc_info=True)
    return UJSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"error": {"code": "request.validation.error", "message": exc.json(indent=0)}},
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(_: Request, __: Exception):
    logger.critical({"status": "internal.server.error"}, exc_info=True)
    return UJSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": {
                "code": "internal.server.error",
                "message": "Internal server error",
            }
        },
    )
