from sqlmodel import SQLModel
from src.application.dtos.ingredientDto import IngredientDto, IngredientProductDto


class CreateProductDto(SQLModel):
    price: int
    name: str
    description: str
    ingredients: list[IngredientProductDto]


class ProductDto(CreateProductDto):
    id: int
