from abc import ABC, abstractmethod
from src.domain.classes.ingredient import Ingredient


class IIngredientRepository(ABC):
    @abstractmethod
    def create_ingredient(self, ingredient: Ingredient) -> Ingredient:
        pass

    @abstractmethod
    def get_all_ingredients(self) -> list[Ingredient]:
        pass

    @abstractmethod
    def get_ingredient_by_id(self, id: int) -> Ingredient:
        pass
