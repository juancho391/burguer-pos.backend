from dataclasses import dataclass
from typing import Optional


@dataclass
class ProductIngredient:
    id_product: int
    id_ingredient: int
    quantity: int
    id: Optional[int] = None

    @classmethod
    def create_new_one(
        cls, id_product: int, id_ingredient: int, quantity: int
    ) -> "ProductIngredient":
        return cls(
            id_product=id_product, id_ingredient=id_ingredient, quantity=quantity
        )

    @classmethod
    def create_from_db(
        cls, id_product: int, id_ingredient: int, quantity: int, id: int
    ) -> "ProductIngredient":
        return cls(
            id_product=id_product, id_ingredient=id_ingredient, quantity=quantity, id=id
        )
