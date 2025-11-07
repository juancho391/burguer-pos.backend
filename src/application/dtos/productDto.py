from sqlmodel import SQLModel
from src.application.dtos.ingredientDto import IngredientDto, IngredientProductDto


class CreateProductDto(SQLModel):
    price: int
    name: str
    description: str
    ingredients: list[IngredientProductDto]


class ProductDto(CreateProductDto):
    id: int


class ProductDtoResponse(SQLModel):
    id: int
    name: str
    description: str
    price: int
    ingredients: list[IngredientDto]


class ProductOrderDto(SQLModel):
    id: int
    quantity: int
