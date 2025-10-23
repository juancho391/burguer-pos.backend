from kink import di
from src.infrastructure.repositories.postgresql_user_repository import (
    PostgreSqlUserRepository,
)
from src.infrastructure.db.db import get_session_database
from src.domain.repositories.userRepository import IUserRepository
from src.application.services.userService import UserService
from src.infrastructure.security.auth import JwtService


def bootstrap_dependencies():
    # Repositories
    user_repository = PostgreSqlUserRepository(session=next(get_session_database()))

    # Services
    jwt_service = JwtService()

    # Dependency Injection
    di[JwtService] = jwt_service
    di[IUserRepository] = user_repository
    di[UserService] = UserService(
        user_repository=user_repository, jwt_service=jwt_service
    )
