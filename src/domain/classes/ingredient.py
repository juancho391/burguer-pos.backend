from dataclasses import dataclass
from typing import Optional


@dataclass
class Ingredient:
    name: str
    stock: int
    reposition_point: Optional[int] = 10
    id: Optional[int] = None

    @classmethod
    def create_new_one(
        cls, name: str, stock: int, reposition_point: int = 10
    ) -> "Ingredient":
        return cls(name=name, stock=stock, reposition_point=reposition_point)

    @classmethod
    def create_from_db(
        cls, id: int, name: str, stock: int, reposition_point: int
    ) -> "Ingredient":
        return cls(id=id, name=name, stock=stock, reposition_point=reposition_point)
