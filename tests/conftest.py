import asyncio
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool

from src.database import get_async_session
from src.database import metadata
from src.config import (DB_HOST_TEST, DB_NAME_TEST, DB_PASS_TEST, DB_PORT_TEST,
                        DB_USER_TEST)
from src.main import app

# DATABASE
DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)                       # create DB engine
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)   # create DB session
metadata.bind = engine_test     # will operate  in test DB


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session

@pytest.fixture(autouse=True, scope='session')           # for DB will be created - used - deleted
async def prepare_database():
    async with engine_test.begin() as conn:              # create DB
        await conn.run_sync(metadata.create_all)           # use metadata fro create all tables
    yield                                                 # give access to tests
    async with engine_test.begin() as conn:               # delete DB
        await conn.run_sync(metadata.drop_all)

# SETUP
@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

client = TestClient(app)                        # this is synchronious test client

@pytest.fixture(scope="session")                       # this is Asynchronious test client
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:   #  create acync client,
        yield ac                                                      # then use it , then client.close

