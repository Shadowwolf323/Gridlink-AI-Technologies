from logging.config import fileConfig
import os
import sys

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Add backend directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import your database
from extensions import db

# Import your Flask app
from app import app

# Alembic Config object
config = context.config

# Logging setup
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Database metadata for migrations
target_metadata = db.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""

    url = app.config.get("SQLALCHEMY_DATABASE_URI")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""

    with app.app_context():

        connectable = db.engine

        with connectable.connect() as connection:

            context.configure(
                connection=connection,
                target_metadata=target_metadata
            )

            with context.begin_transaction():
                context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
