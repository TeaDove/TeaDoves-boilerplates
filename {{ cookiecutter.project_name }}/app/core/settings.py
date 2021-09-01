from pydantic import BaseSettings

class Settings(BaseSettings):
    ssl_on: bool = False
    ssl_keyfile: str = ''
    ssl_certfile: str = ''

    hostname: str = "localhost"
    port: int = 9998
    version: str = "0.0.0"
    project_name: str = "FASTAPI BOILERPLATE"
    fast_api_description: str = 'Small fastapi quickstart app, that can be used anywhere'
    fast_api_log_level: str = "info"

    class Config:
        case_sensitive = False
        env_file = 'conf.d/.env'
        env_file_encoding = 'utf-8'
