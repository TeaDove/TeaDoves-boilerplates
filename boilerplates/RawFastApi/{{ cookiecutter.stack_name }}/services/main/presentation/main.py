from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError, StarletteHTTPException
from fastapi.responses import UJSONResponse
from starlette.exceptions import ExceptionMiddleware

from core.base import logger
from presentation.router import router

app = FastAPI()
app.add_middleware(ExceptionMiddleware, handlers=app.exception_handlers)
app.include_router(router)


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
