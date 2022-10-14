from typing import Any, Dict

from fastapi import FastAPI
from mangum import Mangum
from mangum.handlers import APIGateway
from mangum.types import LambdaConfig, LambdaContext, LambdaEvent

from presentation.main import app


def create_yc_lambda_handler(fastapi_app: FastAPI):
    class YCLambdaContext(LambdaContext):
        token: Dict[str, Any]

    class YCAPIGateway(APIGateway):
        @classmethod
        def infer(cls, event: LambdaEvent, context: YCLambdaContext, config: LambdaConfig) -> bool:
            return "path" in event and "requestContext" in event

        def __init__(self, event: LambdaEvent, context: YCLambdaContext, config: LambdaConfig) -> None:
            super().__init__(event, context, config)

    return Mangum(fastapi_app, custom_handlers=[YCAPIGateway])


yc_lambda_handler = create_yc_lambda_handler(app)
uvicorn_app = app
