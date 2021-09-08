import uvicorn

from .core.settings import Settings


if __name__ == "__main__":
    app_name = "app.api.main:app"
    if Settings().ssl_on:
        uvicorn.run(app_name, host=Settings().hostname, port=Settings().port,
                    log_level=Settings().fast_api_log_level, ssl_certfile=Settings().ssl_certfile,
                    ssl_keyfile=Settings().ssl_keyfile)
    else:
        uvicorn.run(app_name, host=Settings().hostname, port=Settings().port,
                    log_level=Settings().fast_api_log_level)