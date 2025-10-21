from abc import ABC, abstractmethod
from src.domain.classes.user import User


class IUserRepository(ABC):
    @abstractmethod
    def add_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> User | None:
        pass
