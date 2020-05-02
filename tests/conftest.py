from typing import Generator, Dict

import pytest
from starlette.testclient import TestClient

from b_riders import crud
from b_riders.api import app
from b_riders.core.config import settings
from b_riders.db.session import SessionLocal
from b_riders.schemas import UserCreate


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.TEST_SUPERUSER,
        "password": settings.TEST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers


@pytest.fixture(scope="module")
def superuser_token_headers(db, client: TestClient) -> Dict[str, str]:
    if not crud.user.get_by_email(db, email=settings.TEST_SUPERUSER):
        crud.user.create(
            db,
            obj_in=UserCreate(
                email=settings.TEST_SUPERUSER, password=settings.TEST_SUPERUSER_PASSWORD
            ),
        )
    return get_superuser_token_headers(client)
