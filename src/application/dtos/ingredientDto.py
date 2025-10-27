from sqlmodel import SQLModel
from typing import Optional


class CreateIngredientDto(SQLModel):
    name: str
    stock: int
    reposition_point: int


class IngredientDto(CreateIngredientDto):
    id: int
