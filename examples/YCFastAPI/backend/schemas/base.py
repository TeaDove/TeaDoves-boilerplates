import ujson
from pydantic import BaseModel


class ConfigBaseModel(BaseModel):
    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        use_enum_values = True
        json_loads = ujson.loads
        json_dumps = ujson.dumps
