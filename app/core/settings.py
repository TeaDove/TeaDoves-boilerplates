from pydantic import BaseSettings

class Settings(BaseSettings):
    ssl_on: bool = False
    ssl_keyfile: str = ''
    ssl_certfile: str = ''

    api_hostname: str = "localhost"
    api_port: int = 9998
    version: str = "0.0.0"
    project_name: str = "FASTAPI BOILERPLATE"
    fast_api_description: str = 'Small fastapi quickstart app, that can be used anywhere'
    fast_api_log_level: str = "info"

    class Config:
        case_sensitive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'
