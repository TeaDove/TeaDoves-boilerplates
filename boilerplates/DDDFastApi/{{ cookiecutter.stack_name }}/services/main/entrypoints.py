from mangum import Mangum

from core.settings import app_settings
from presentation.main import app as fastapi_app

lambda_api_handler = Mangum(fastapi_app, api_gateway_base_path=app_settings.base_apigw_path)
uvicorn_app = fastapi_app
