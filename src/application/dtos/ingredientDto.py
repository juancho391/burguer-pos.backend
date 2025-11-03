from sqlmodel import SQLModel


class CreateIngredientDto(SQLModel):
    name: str
    stock: int
    reposition_point: int


class IngredientDto(CreateIngredientDto):
    id: int


class IngredientProductDto(IngredientDto):
    quantity: int
