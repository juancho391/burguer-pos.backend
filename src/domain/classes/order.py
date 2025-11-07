from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from src.domain.classes.product import Product


@dataclass
class Order:
    id_user: int
    customer_name: str
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    total_price: Optional[float] = None
    service_price: Optional[float] = None
    products: Optional[List[Product]] = None

    @classmethod
    def create_new_one(
        cls,
        id_user: int,
        customer_name: str,
        products: List[Product],
        include_service: bool,
        service_rate: float = 0.10,
    ):
        created_at = datetime.now()

        total_products_price = sum(p.price for p in products)

        if not include_service:
            return cls(
                id_user=id_user,
                customer_name=customer_name,
                created_at=created_at,
                total_price=total_products_price,
                service_price=0,
                products=products,
            )

        service_price = total_products_price * service_rate

        total_price = total_products_price + service_price

        return cls(
            id_user=id_user,
            customer_name=customer_name,
            created_at=created_at,
            total_price=total_price,
            service_price=service_price,
            products=products,
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
