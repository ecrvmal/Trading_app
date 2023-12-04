from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

<<<<<<< HEAD
import os
import sys

sys.path.append(os.path.join(sys.path[0], 'src'))

from src.config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASS
from src.auth.models import metadata as metadata_auth
from src.operations.models import metadata as metadata_operations
=======
from config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASS  # New
from models.models import metadata
>>>>>>> 3ee3f0bdc4f63aabcbed87be2a9fd8c5d78ab85d

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

<<<<<<< HEAD
section = config.config_ini_section
config.set_section_option(section, "DB_HOST", DB_HOST)
config.set_section_option(section, "DB_PORT", DB_PORT)
config.set_section_option(section, "DB_USER", DB_USER)
config.set_section_option(section, "DB_NAME", DB_NAME)
config.set_section_option(section, "DB_PASS", DB_PASS)
=======
section = config.config_ini_section                           # New
config.set_section_option(section, "DB_HOST", DB_HOST)        # New
config.set_section_option(section, "DB_PORT", DB_PORT)        # New
config.set_section_option(section, "DB_USER", DB_USER)        # New
config.set_section_option(section, "DB_NAME", DB_NAME)        # New
config.set_section_option(section, "DB_PASS", DB_PASS)        # New
>>>>>>> 3ee3f0bdc4f63aabcbed87be2a9fd8c5d78ab85d

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
<<<<<<< HEAD
target_metadata = [metadata_auth, metadata_operations]
=======


# target_metadata = None
target_metadata = metadata                                    # new

>>>>>>> 3ee3f0bdc4f63aabcbed87be2a9fd8c5d78ab85d

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
