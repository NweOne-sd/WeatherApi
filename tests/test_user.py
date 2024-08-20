from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "Test User", "email": "test@example.com", "city": "London", "state": "UK"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"
