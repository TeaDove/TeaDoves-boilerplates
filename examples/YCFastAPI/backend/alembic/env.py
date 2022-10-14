from logging.config import fileConfig

from alembic import context
from geoalchemy2.alembic_helpers import include_object, render_item
from pydantic import PostgresDsn
from sqlalchemy import engine_from_config, pool

from core.settings import db_settings
from persistence.base import Base, BaseModel
from persistence.camera import Camera, ParkingLotCamera  # noqa F401
from persistence.user import User  # noqa F401

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

dsn = PostgresDsn.build(
    scheme="postgresql",
    host=db_settings.dsn.host,
    port=db_settings.dsn.port,
    user=db_settings.dsn.user,
    password=db_settings.dsn.password,
    path=db_settings.dsn.path,
)
config.set_main_option("sqlalchemy.url", dsn)

target_schema = BaseModel.__table_args__["schema"]
version_table_schema = "alembic"
version_table = f"{target_schema}_versions"
target_metadata = Base.metadata


def include_name(name, type_, parent_names):
    if type_ == "schema":
        return name == target_schema
    else:
        return True


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            render_item=render_item,
            include_object=include_object,
            target_metadata=target_metadata,
            include_schemas=True,
            include_name=include_name,
            version_table_schema=version_table_schema,
            version_table=version_table,
        )
        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
