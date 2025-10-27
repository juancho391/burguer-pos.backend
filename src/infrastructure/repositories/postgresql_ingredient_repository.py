from src.domain.classes.ingredient import Ingredient
from src.domain.repositories.ingredientRepository import IIngredientRepository
from sqlmodel import Session
from src.infrastructure.models.ingredientModel import IngredientModel
from src.application.dtos.ingredientDto import CreateIngredientDto


class PostgreSqlIngredientRepository(IIngredientRepository):

    def __init__(self, session: Session) -> None:
        self.session = session

    def create_ingredient(self, ingredient: Ingredient) -> Ingredient:
        ingredient_model = IngredientModel.model_validate(
            CreateIngredientDto(**ingredient.__dict__)
        )
        self.session.add(ingredient_model)
        self.session.commit()
        self.session.refresh(ingredient_model)
        return Ingredient.create_from_db(**ingredient_model.model_dump())
