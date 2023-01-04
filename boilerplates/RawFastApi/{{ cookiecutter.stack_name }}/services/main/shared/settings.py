from pydantic import BaseSettings


class _Settings(BaseSettings):
    log_level: str = "INFO"

    class Config:
        env_file = ".env"


class _AppSettings(BaseSettings):
    local_run: bool = False
    show_swagger: bool = False

    class Config:
        env_file = ".env"
        env_prefix = "app_"


settings = _Settings()
app_settings = _AppSettings()
