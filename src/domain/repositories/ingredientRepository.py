from abc import ABC, abstractmethod
from src.domain.classes.ingredient import Ingredient


class IIngredientRepository(ABC):
    @abstractmethod
    def create_ingredient(self, ingredient: Ingredient) -> Ingredient:
        pass
