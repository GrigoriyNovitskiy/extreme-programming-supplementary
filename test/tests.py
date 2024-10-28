from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_root(client):
    response = client.get("/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "API is live"}


def test_create_get_user(client):
    response = client.post("/register/", json={
        "login": "Roman",
        "email": "roman@mail",
        "password": "Password"
    })
    assert response.status_code == 201

    response = client.get(f"/users/0")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["Status"] == "Success"
    assert response_json["User"]["login"] == "Roman"
    assert response_json["User"]["email"] == "roman@mail"