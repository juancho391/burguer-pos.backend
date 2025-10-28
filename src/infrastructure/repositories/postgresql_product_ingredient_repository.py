from sqlmodel import Session
from src.application.dtos.productIngredientDto import ProductIngredientDto
from src.domain.classes.productIngredient import ProductIngredient
from src.domain.repositories.productIngredientRepository import (
    IProductIngredientRepository,
)
from src.infrastructure.models.productIngredientModel import ProductIngredientModel


class ProductIngredientRepository(IProductIngredientRepository):

    def __init__(self, session: Session) -> None:
        self.session = session

    def create_product_ingredient(
        self, product_ingredient: ProductIngredient
    ) -> ProductIngredient:
        product_ingredient_model = ProductIngredientModel.model_validate(
            ProductIngredientDto(**product_ingredient.__dict__)
        )
        self.session.add(product_ingredient_model)
        self.session.commit()
        self.session.refresh(product_ingredient_model)
        return ProductIngredient.create_from_db(**product_ingredient_model.model_dump())

    def create_all_product_ingredients(
        self, product_ingredients: list[ProductIngredient]
    ):
        product_ingredients_models = [
            ProductIngredientModel.model_validate(
                ProductIngredientDto(**product_ingredient.__dict__)
            )
            for product_ingredient in product_ingredients
        ]
        self.session.add_all(product_ingredients_models)
        self.session.commit()
        return True
