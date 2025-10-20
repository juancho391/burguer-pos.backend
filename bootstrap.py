from kink import di
from src.infrastructure.repositories.postgresql_repository import (
    PostgreSQLRepositoryImpl,
)
from src.infrastructure.db.db import get_session_database
from src.domain.repositories.userRepository import IFakeUserRepository
from src.application.services.userService import UserService


def bootstrap_dependencies():
    user_repository = PostgreSQLRepositoryImpl(session=next(get_session_database()))
    di[IFakeUserRepository] = user_repository
    di[UserService] = UserService(user_repository=user_repository)
