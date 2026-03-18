import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_content_returns_draft():
    response = client.post(
        "/api/v1/content/",
        json={"topic": "New art exhibition", "platform": "instagram", "tone": "creative"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert data["data"]["platform"] == "instagram"
    assert data["data"]["status"] == "draft"


def test_create_content_has_id():
    response = client.post(
        "/api/v1/content/",
        json={"topic": "Art", "platform": "twitter"},
    )
    assert response.status_code == 200
    assert "id" in response.json()["data"]


def test_create_content_missing_required_field():
    response = client.post("/api/v1/content/", json={"platform": "twitter"})
    assert response.status_code == 422


def test_create_content_invalid_platform():
    response = client.post(
        "/api/v1/content/",
        json={"topic": "Art", "platform": "myspace"},
    )
    assert response.status_code == 422


def test_list_content_returns_empty_list():
    response = client.get("/api/v1/content/")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
