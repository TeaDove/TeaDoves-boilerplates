from pydantic import BaseSettings


class _AppSettings(BaseSettings):
    hostname: str = "localhost"
    port: int = 8000
    base_apigw_path: str = "/v0"
    show_swagger: bool = False

    class Config:
        env_file = ".env"
        env_prefix = "app_"


app_settings = _AppSettings()
