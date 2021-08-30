from pydantic import BaseModel


class HelloWorld(BaseModel):
    Hello: str = "World"
    your_ip: str = "127.0.0.1"
