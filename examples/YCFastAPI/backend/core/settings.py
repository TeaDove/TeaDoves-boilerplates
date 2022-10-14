from typing import Optional

from pydantic import BaseSettings, PostgresDsn


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


class _DBSettings(BaseSettings):
    dsn: PostgresDsn
    autocommit: bool = False

    class Config:
        env_file = ".env"
        env_prefix = "db_"


class _SecuritySettings(BaseSettings):
    yc_token: Optional[str] = None
    yc_access_key: Optional[str] = None
    yc_secret_key: Optional[str] = None

    class Config:
        env_file = ".env"
        env_prefix = "security_"


db_settings = _DBSettings()
settings = _Settings()
app_settings = _AppSettings()
security_settings = _SecuritySettings()
