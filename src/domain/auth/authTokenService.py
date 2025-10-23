from abc import ABC, abstractmethod
from src.domain.classes.token import Token


class AuthTokenService(ABC):
    @abstractmethod
    def create_access_token(self, user_id: int, email: str) -> Token:
        pass

    @abstractmethod
    def verify_token(self, token: Token) -> Token:
        pass
