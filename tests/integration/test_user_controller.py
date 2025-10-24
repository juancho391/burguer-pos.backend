from fastapi.testclient import TestClient
from tests.boostrap_test import bootstrap_dependencies_test
from src.main import app


class TestUserController:
    bootstrap_dependencies_test()
    client = TestClient(app)

    def test_create_user_integration_success(self):

        payload = {
            "name": "Jane Doe 2",
            "email": "janedoe2@gmail.com",
            "password": "janedoe1234",
        }
        response = self.client.post("auth/register/", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == payload["name"]
        assert data["email"] == payload["email"]
        assert "id" in data

    def test_authenticate_user_integration_success(self):
        self.test_create_user_integration_success()
        login_payload = {
            "email": "janedoe2@gmail.com",
            "password": "janedoe1234",
        }
        response = self.client.post("auth/token/", json=login_payload)
        assert response.status_code == 200
        assert "token" in response.json()
