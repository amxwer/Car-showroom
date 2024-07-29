import asyncio
from functools import wraps
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from config import DB_USER_TEST, DB_PASS_TEST, DB_HOST_TEST, DB_PORT_TEST, DB_NAME_TEST
from src.main import app
from src import metadata
from database import get_async_session



DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

engine_test = create_async_engine(DATABASE_URL_TEST,poolclass=NullPool)
async_session_maker = sessionmaker(
    engine_test,
    class_=AsyncSession,
    expire_on_commit=False
)

metadata.bind = engine_test
async def override_get_async_session() ->AsyncGenerator[AsyncSession,None]:
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session

@pytest.fixture(autouse=True,scope='session')
async def prepare_database():
    async with engine_test.begin() as connection:
        await connection.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as connection:
        await connection.run_sync(metadata.drop_all)



@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

client = TestClient(app)


@pytest.fixture(scope="session")
async def ac():
    # need to load app module after mock. otherwise, it would fail
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
