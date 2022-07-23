import humps
import ujson
from pydantic import BaseModel
from pydantic.generics import GenericModel


class ConfigBaseModel(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = humps.camelize
        orm_mode = True
        use_enum_values = True
        json_loads = ujson.loads
        json_dumps = ujson.dumps


class GenericConfigBaseModel(GenericModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = humps.camelize
        orm_mode = True
        use_enum_values = True
        json_loads = ujson.loads
        json_dumps = ujson.dumps
