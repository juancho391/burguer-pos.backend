from abc import ABC, abstractmethod
from src.domain.classes.productIngredient import ProductIngredient


class IProductIngredientRepository(ABC):
    @abstractmethod
    def create_product_ingredient(
        self, product_ingredient: ProductIngredient
    ) -> ProductIngredient:
        pass

    @abstractmethod
    def create_all_product_ingredients(
        self, product_ingredients: list[ProductIngredient]
    ) -> bool:
        pass
