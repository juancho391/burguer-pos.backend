from fastapi.testclient import TestClient
from tests.boostrap_test import bootstrap_dependencies_test
from src.main import app


bootstrap_dependencies_test()
client = TestClient(app)


def test_create_user_integration_success():

    payload = {
        "name": "Jane Doe 2",
        "email": "janedoe2@gmail.com",
        "password": "janedoe1234",
    }
    response = client.post("auth/register/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert "id" in data
