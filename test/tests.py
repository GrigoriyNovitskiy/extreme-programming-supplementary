from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root(client):
    response = client.get("/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "API is live"}


def test_create_get_user(client):
    response = client.post("/register/", json={
      "id": 0,
      "first_name": "Roman",
      "last_name": "Povolotskii",
      "password": "Password"
    })
    assert response.status_code == 201

    response = client.get(f"/users/{response.json()['id']}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["Status"] == "Success"
    assert response_json["User"]["first_name"] == "Roman"
    assert response_json["User"]["last_name"] == "Povolotskii"