from sqlmodel import SQLModel
from src.application.dtos.ingredientDto import IngredientDto


class CreateProductDto(SQLModel):
    price: int
    name: str
    description: str
    ingredients: list[IngredientDto]


class ProductDto(CreateProductDto):
    id: int
