import pytest
from src.application.services.userService import UserService
from src.infrastructure.repositories.postgresql_user_repository import (
    PostgreSqlUserRepository,
)
from tests.conftest import get_session_test
from src.infrastructure.security.auth import JwtService
from src.application.dtos.userDto import CreateUserDto, UserDto, UserLoginDto
from src.application.dtos.tokenDto import TokenDto


class TestUserService:
    repository = PostgreSqlUserRepository(session=next(get_session_test()))
    user_service = UserService(user_repository=repository, jwt_service=JwtService())
    user_dto = CreateUserDto(
        name="Jhon Doe", email="jhondoe@gmail.com", password="jhondoe123"
    )

    def test_create_user_success(self):
        result = self.user_service.create_user(new_user=self.user_dto)
        assert result.name == self.user_dto.name
        assert result.email == self.user_dto.email
        assert isinstance(result, UserDto)
        assert result.id is not None

    def test_create_user_already_exists(self):
        self.user_service.create_user(new_user=self.user_dto)
        with pytest.raises(Exception) as exc_info:
            self.user_service.create_user(new_user=self.user_dto)
        assert (
            str(exc_info.value)
            == "A user with the email 'jhondoe@gmail.com' already exists."
        )

    def test_authenticate_user_success(self):
        self.user_service.create_user(
            new_user=CreateUserDto(
                name=self.user_dto.name,
                email=self.user_dto.email,
                password=str(self.user_dto.password),
            )
        )
        user_login_dto = UserLoginDto(
            email=self.user_dto.email, password=str(self.user_dto.password)
        )
        result = self.user_service.authenticate_user(user=user_login_dto)

        assert result.access_token is not None
        assert isinstance(result, TokenDto)

    def test_authenticate_user_invalid_password(self):
        self.user_service.create_user(new_user=self.user_dto)
        user_login_dto = UserLoginDto(
            email=self.user_dto.email, password="invalid_password"
        )
        with pytest.raises(Exception) as exc_info:
            self.user_service.authenticate_user(user=user_login_dto)
        assert str(exc_info.value) == "Invalid email or password."

    def test_authenticate_user_invalid_email(self):
        self.user_service.create_user(new_user=self.user_dto)
        user_login_dto = UserLoginDto(
            email="invalidemail@gmail.com", password=str(self.user_dto.password)
        )
        with pytest.raises(Exception) as exc_info:
            self.user_service.authenticate_user(user=user_login_dto)
        assert str(exc_info.value) == "Invalid email or password."
