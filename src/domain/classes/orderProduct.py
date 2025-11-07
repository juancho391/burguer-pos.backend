from dataclasses import dataclass
from typing import Optional


@dataclass
class OrderProduct:
    quantity: int
    unit_price: int
    product_id: int
    order_id: int
    id: Optional[int] = None

    @classmethod
    def create_new_one(
        cls, quantity: int, unit_price: int, product_id: int, order_id: int
    ) -> "OrderProduct":
        return cls(
            quantity=quantity,
            unit_price=unit_price,
            product_id=product_id,
            order_id=order_id,
        )

    @classmethod
    def create_from_db(
        cls, quantity: int, unit_price: int, product_id: int, order_id: int, id: int
    ) -> "OrderProduct":
        return cls(
            quantity=quantity,
            unit_price=unit_price,
            product_id=product_id,
            order_id=order_id,
            id=id,
        )
