from sqlmodel import SQLModel


class TokenDto(SQLModel):
    access_token: str
    token_type: str
