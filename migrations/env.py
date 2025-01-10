from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.models import Base
from app.database import engine


# Interpret the config file for Python logging.
fileConfig(context.config.config_file_name)


target_metadata = Base.metadata


def run_migrations_online():
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
