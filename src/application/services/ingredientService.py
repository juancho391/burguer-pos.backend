from kink import inject
from src.domain.repositories.ingredientRepository import IIngredientRepository
from src.infrastructure.security.auth import JwtService
from src.application.dtos.ingredientDto import CreateIngredientDto, IngredientDto
from src.domain.classes.ingredient import Ingredient


@inject
class IngredientService:

    def __init__(self, repository: IIngredientRepository) -> None:
        self.repository = repository

    def create_ingredient(self, new_ingredient: CreateIngredientDto) -> IngredientDto:
        ingredient_entity = Ingredient.create_new_one(
            name=new_ingredient.name,
            stock=new_ingredient.stock,
            reposition_point=new_ingredient.reposition_point,
        )
        ingredient_created = self.repository.create_ingredient(ingredient_entity)
        return IngredientDto(**ingredient_created.__dict__)

    def get_all_ingredients(self, limit: int) -> list[IngredientDto]:
        ingredients = self.repository.get_all_ingredients(limit=limit)
        return [IngredientDto(**ingredient.__dict__) for ingredient in ingredients]
