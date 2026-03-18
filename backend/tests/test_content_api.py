from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_content():
    response = client.post(
        "/api/v1/content/",
        json={"topic": "New art exhibition", "platform": "instagram", "tone": "creative"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert data["data"]["platform"] == "instagram"
    assert data["data"]["status"] == "draft"


def test_list_content():
    response = client.get("/api/v1/content/")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
