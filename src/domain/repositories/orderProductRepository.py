from abc import ABC, abstractmethod
from src.domain.classes.orderProduct import OrderProduct


class IOrderProductRepository(ABC):
    @abstractmethod
    def create_all_order_product(self, order_products: list[OrderProduct]) -> bool:
        pass

    @abstractmethod
    def add_product_to_order(self, order_product: OrderProduct) -> bool:
        pass
