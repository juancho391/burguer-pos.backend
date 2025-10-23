from src.domain.auth.hasher import IPasswordHasher
from pwdlib import PasswordHash


class PasswordHasher(IPasswordHasher):
    password_hash = PasswordHash.recommended()

    @staticmethod
    def hash_password(password: str) -> str:
        return PasswordHasher.password_hash.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return PasswordHasher.password_hash.verify(plain_password, hashed_password)
