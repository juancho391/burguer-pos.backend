from abc import ABC, abstractmethod
from src.domain.classes.product import Product


class IProductRepository(ABC):
    @abstractmethod
    def create_product(self, product: Product) -> Product:
        pass

    @abstractmethod
    def get_all_products(self, limit: int) -> list[Product]:
        pass

    @abstractmethod
    def get_product_by_id(self, id: int) -> Product | None:
        pass

    @abstractmethod
    def delete_product(self, id: int) -> bool:
        pass
