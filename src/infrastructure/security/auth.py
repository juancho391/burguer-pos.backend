from src.domain.classes.token import Token
from src.domain.auth.authTokenService import AuthTokenService
import os
import jwt
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from src.domain.classes.token import TokenData
from src.domain.errors.errors import AuthenticationError
from fastapi import Depends
from typing import Annotated

load_dotenv()


class JwtService(AuthTokenService):
    JWT_SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

    def create_access_token(self, user_id: int, email: str) -> Token:
        expires_at = datetime.now(timezone.utc) + timedelta(
            minutes=int(str(self.JWT_ACCESS_TOKEN_EXPIRE_MINUTES))
        )
        payload = {"sub": str(user_id), "email": email, "exp": expires_at}  # type: ignore
        token_value = jwt.encode(  # type: ignore
            payload, self.JWT_SECRET_KEY.encode(), algorithm=self.JWT_ALGORITHM  # type: ignore
        )
        return Token(access_token=token_value, token_type="bearer")

    def verify_token(self, token: Token) -> TokenData:
        try:
            payload = jwt.decode(  # type: ignore
                token, self.JWT_SECRET_KEY, algorithms=[self.JWT_ALGORITHM]  # type: ignore
            )
            return TokenData(email=payload.get("email"))
        except jwt.ExpiredSignatureError:
            raise AuthenticationError("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationError("Invalid Token")

    def get_current_user(
        self, token: Annotated[Token, Depends(oauth2_scheme)]
    ) -> TokenData:
        return self.verify_token(token=token)


Current_user = Annotated[TokenData, Depends(JwtService().get_current_user)]
