from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from src.domain.classes.product import Product


@dataclass
class Order:
    id_user: int
    customer_name: str
    id: Optional[int] = None
    created_at: Optional[datetime] = datetime.now()
    total_price: Optional[int] = 0
    service_price: Optional[int] = 0
    products: Optional[List[Product]] = None

    @classmethod
    def create_new_one(
        cls,
        id_user: int,
        customer_name: str,
    ):

        return cls(
            id_user=id_user,
            customer_name=customer_name,
        )

    @classmethod
    def create_from_db(
        cls,
        id: int,
        id_user: int,
        customer_name: str,
        created_at: datetime,
        total_price: float,
        service_price: float,
        products: List[Product],
    ):
        return cls(
            id=id,
            id_user=id_user,
            customer_name=customer_name,
            created_at=created_at,
            total_price=total_price,
            service_price=service_price,
            products=products,
        )
