from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from b_riders import crud
from b_riders.core.config import settings
from b_riders.schemas import ClassificationCreate


def test_create_classification(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"description": "teste"}
    response = client.post(
        f"{settings.API_V1_STR}/classification/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    cf = response.json()
    assert cf["description"] == data["description"]
    assert "id" in cf


def test_create_ride(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    classification = crud.classifications.create(
        db, obj_in=ClassificationCreate(description="Teste")
    )
    data = {
        "begin": "2020-05-02T01:16:17.243000",
        "end": "2020-05-02T01:16:17.243000",
        "experience": 2,
        "classification_id": classification.id,
    }
    response = client.post(
        f"{settings.API_V1_STR}/rides/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    cf = response.json()
    assert "id" in cf
