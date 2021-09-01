from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from .models import HelloWorld
from ..core.settings import Settings

app = FastAPI(title=Settings().project_name, version=Settings().version, description=Settings().fast_api_description)

# FIXME: менять в проде allow_origins на локальные!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    logger.info(f"Docs: http://{Settings().hostname}:{Settings().port}/docs")


# Заглушка на /
@app.get('/', response_model=HelloWorld)
async def hello_world(request: Request):
    """
    Заглушка для демонстрации работы сервера
    """
    return {'Hello': 'World', "your ip": request.client.host}
