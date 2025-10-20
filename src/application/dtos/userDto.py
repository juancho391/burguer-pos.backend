from sqlmodel import SQLModel
from pydantic import EmailStr


class CreateUserDto(SQLModel):
    name: str
    email: EmailStr
    password: str


class UserDto(SQLModel):
    id: int
    name: str
    email: str
