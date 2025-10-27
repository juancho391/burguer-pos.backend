from abc import ABC, abstractmethod
from src.domain.classes.product import Product


class IProductRepository(ABC):
    @abstractmethod
    def create_product(self, product: Product) -> Product:
        pass
