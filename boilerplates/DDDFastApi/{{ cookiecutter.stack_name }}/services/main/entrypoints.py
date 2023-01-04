from mangum import Mangum

from presentation.main import app as fastapi_app
from shared.settings import app_settings

lambda_api_handler = Mangum(fastapi_app, api_gateway_base_path=app_settings.base_apigw_path)
uvicorn_app = fastapi_app
