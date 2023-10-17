from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_list():
    response = client.get("/user/list")
    assert response.status_code == 200
    assert response.json()[0]["id"] == 1
    