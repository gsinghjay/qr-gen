"""Test configuration and fixtures."""

import asyncio
from typing import AsyncGenerator, Generator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings
from app.core.database import Base, get_db
from app.main import create_app

# Test database URL
TEST_DATABASE_URL = settings.DATABASE_URL.replace(
    settings.DATABASE_NAME, f"{settings.DATABASE_NAME}_test"
)

# Create async engine for tests
engine = create_async_engine(
    TEST_DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)
TestingSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

@pytest.fixture(scope="session")
def event_loop() -> Generator:
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def app() -> FastAPI:
    """Create a fresh database on each test case."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    app = create_app()

    # Dependencies override
    async def override_get_db() -> AsyncGenerator[AsyncSession, None]:
        async with TestingSessionLocal() as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db

    return app

@pytest.fixture(scope="session")
async def client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """Create a new FastAPI TestClient that uses the `db_session` fixture."""
    async with AsyncClient(
        app=app,
        base_url="http://test",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client

@pytest.fixture(scope="session")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """Create a new database session for a test."""
    async with TestingSessionLocal() as session:
        yield session

@pytest.fixture(scope="function", autouse=True)
async def auto_rollback(db_session: AsyncSession) -> AsyncGenerator[None, None]:
    """Automatically rollback database changes after each test."""
    async with db_session.begin():
        yield
        await db_session.rollback() 