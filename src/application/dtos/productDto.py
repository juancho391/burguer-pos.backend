from sqlmodel import SQLModel
from src.application.dtos.ingredientDto import IngredientDto, IngredientProductDto


# Dto for creating a new product
class CreateProductDto(SQLModel):
    price: int
    name: str
    description: str
    ingredients: list[IngredientProductDto]


# Dto for validating product from db o response without ingredients
class ProductDto(CreateProductDto):
    id: int


class ProductDtoResponse(SQLModel):
    id: int
    name: str
    description: str
    price: int
    ingredients: list[IngredientDto]


# Dto for adding products to an order
class ProductOrderDto(SQLModel):
    id: int
    quantity: int


class ProductNoIngredientsDto(SQLModel):
    id: int
    name: str
    description: str
    price: int
