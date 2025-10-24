from kink import di
from src.infrastructure.repositories.postgresql_user_repository import (
    PostgreSqlUserRepository,
)
from src.application.services.userService import UserService
from src.infrastructure.security.auth import JwtService
from tests.conftest import get_session_test
from src.domain.repositories.userRepository import IUserRepository


def bootstrap_dependencies_test():
    # Repositorio con sesión de prueba
    session = next(get_session_test())
    user_repository = PostgreSqlUserRepository(session=session)

    # Servicio JWT
    jwt_service = JwtService()

    # Sobrescribir dependencias en Kink
    di[IUserRepository] = user_repository
    di[UserService] = UserService(
        user_repository=user_repository, jwt_service=jwt_service
    )
    di[JwtService] = jwt_service
