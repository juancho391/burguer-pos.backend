from dataclasses import dataclass
from pydantic import EmailStr
from typing import Optional, Type


@dataclass
class User:
    name: str
    email: EmailStr
    password: str
    id: Optional[int] = None

    @classmethod
    def create_new_one(cls, name: str, email: EmailStr, password: str) -> "User":
        return cls(name=name, email=email, password=password)  # type: ignore

    @classmethod
    def create_from_db(
        cls: "Type[User]", id: int, name: str, email: EmailStr, password: str
    ) -> "User":
        return cls(id=id, name=name, email=email, password=password)
