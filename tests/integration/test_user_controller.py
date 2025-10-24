from fastapi.testclient import TestClient
from tests.boostrap_test import bootstrap_dependencies_test
from src.main import app


class TestUserController:
    bootstrap_dependencies_test()
    client = TestClient(app)
    register_payload = {
        "name": "Jane Doe",
        "email": "janedoe@gmail.com",
        "password": "janedoe123",
    }
    login_payload = {
        "email": "janedoe@gmail.com",
        "password": "janedoe123",
    }

    def test_create_user_integration_success(self):
        response = self.client.post("auth/register/", json=self.register_payload)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == self.register_payload["name"]
        assert data["email"] == self.register_payload["email"]
        assert "id" in data

    def test_create_user_already_exists_integration_error(self):
        self.test_create_user_integration_success()
        response = self.client.post("auth/register/", json=self.register_payload)
        assert response.status_code == 400
        assert (
            response.json()["detail"]
            == f"A user with the email '{self.register_payload['email']}' already exists."
        )

    def test_authenticate_user_integration_success(self):
        self.test_create_user_integration_success()
        response = self.client.post("auth/token/", json=self.login_payload)
        assert response.status_code == 200
        assert "token" in response.json()
