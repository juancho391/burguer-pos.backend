from sqlmodel import SQLModel, Field  # type: ignore
from pydantic import EmailStr


class CreateUserDto(SQLModel):
    name: str = Field(min_length=4, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=30)


class UserDto(SQLModel):
    id: int
    name: str
    email: str
