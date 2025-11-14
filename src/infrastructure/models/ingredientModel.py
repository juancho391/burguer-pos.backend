from sqlmodel import (
    Field,  # pyright: ignore[reportUnknownVariableType]
    SQLModel,
    Relationship,
)
from src.infrastructure.models.productIngredientModel import ProductIngredientModel


class IngredientModel(SQLModel, table=True):
    __tablename__ = "Ingredients"

    id: int = Field(default=None, primary_key=True)
    name: str
    stock: int | None = 0
    reposition_point: int

    products_links: list[ProductIngredientModel] = Relationship(
        back_populates="ingredient", cascade_delete=True
    )
