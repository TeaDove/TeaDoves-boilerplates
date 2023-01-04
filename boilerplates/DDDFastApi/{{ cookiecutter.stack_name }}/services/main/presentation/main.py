from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError, StarletteHTTPException
from fastapi.responses import UJSONResponse
from starlette.exceptions import ExceptionMiddleware

from presentation.router import router
from shared.base import logger
from shared.settings import app_settings


def create_app() -> FastAPI:
    if app_settings.show_swagger:
        fastapi_app = FastAPI()
    else:
        fastapi_app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

    fastapi_app.add_middleware(ExceptionMiddleware, handlers=fastapi_app.exception_handlers)
    fastapi_app.include_router(router)
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
