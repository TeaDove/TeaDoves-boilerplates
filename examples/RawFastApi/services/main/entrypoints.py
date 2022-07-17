import uvicorn

from core.settings import app_settings
from presentation.main import app as fastapi_app

if __name__ == "__main__":
    uvicorn.run(fastapi_app, host=app_settings.hostname, port=app_settings.port)
