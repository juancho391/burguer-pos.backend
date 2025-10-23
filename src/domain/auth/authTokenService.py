from abc import ABC, abstractmethod
from src.domain.classes.token import Token, TokenData


class AuthTokenService(ABC):
    @abstractmethod
    def create_access_token(self, user_id: int, email: str) -> Token:
        pass

    @abstractmethod
    def verify_token(self, token: Token) -> TokenData:
        pass

    @abstractmethod
    def get_current_user(self, token: Token) -> TokenData:
        pass
