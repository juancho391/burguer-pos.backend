from src.domain.classes.token import Token
from src.domain.auth.authTokenService import AuthTokenService
import os
import jwt
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv

load_dotenv()


class JwtService(AuthTokenService):
    JWT_SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    JWT_ALGORITHM = os.getenv("ALGORITHM")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

    def create_access_token(self, user_id: int, email: str) -> Token:
        expires_at = datetime.now(timezone.utc) + timedelta(
            minutes=int(str(self.JWT_ACCESS_TOKEN_EXPIRE_MINUTES))
        )
        payload = {"sub": user_id, "email": email, "exp": expires_at}  # type: ignore
        token_value = jwt.encode(  # type: ignore
            payload, self.JWT_SECRET_KEY.encode(), algorithm=self.JWT_ALGORITHM  # type: ignore
        )
        return Token(access_token=token_value, token_type="bearer")

    def verify_token(self, token: Token) -> Token:
        try:
            return jwt.decode(  # type: ignore
                token.access_token, self.JWT_SECRET_KEY, algorithms=[self.JWT_ALGORITHM]  # type: ignore
            )
        except jwt.ExpiredSignatureError:
            raise Exception("Token expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")
