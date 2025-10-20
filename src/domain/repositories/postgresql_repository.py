from abc import ABC, abstractmethod
from src.domain.classes.user import User


class PostgreSQLRepository(ABC):
    @abstractmethod
    def add_user(self, user: User) -> User:
        pass
