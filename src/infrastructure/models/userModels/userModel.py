from sqlmodel import Field, SQLModel  # pyright: ignore[reportUnknownVariableType]
from pydantic import EmailStr


class UserModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, max_length=100)
    email: EmailStr = Field(index=True, unique=True, nullable=False)
    password: str
