from dataclasses import dataclass
from typing import Optional
from src.domain.classes.ingredient import Ingredient
from src.domain.errors.errors import PriceZeroError


@dataclass
class Product:
    name: str
    description: str
    price: int
    ingredients: list[Ingredient]
    id: Optional[int] = None

    @classmethod
    def create_new_one(
        cls, name: str, description: str, price: int, ingredients: list[Ingredient]
    ) -> "Product":
        if price <= 0:
            raise PriceZeroError()
        return cls(
            name=name, description=description, price=price, ingredients=ingredients
        )

    @classmethod
    def create_from_db(
        cls,
        id: int,
        name: str,
        description: str,
        price: int,
        ingredients: list[Ingredient] = [],
    ):
        return cls(
            id=id,
            name=name,
            description=description,
            price=price,
            ingredients=ingredients,
        )
