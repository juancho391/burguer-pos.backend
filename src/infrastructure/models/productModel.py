from sqlmodel import (
    Field,  # pyright: ignore[reportUnknownVariableType]
    SQLModel,
    Relationship,
)
from src.infrastructure.models.productIngredientModel import ProductIngredientModel


class ProductModel(SQLModel, table=True):
    __tablename__ = "Products"

    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, max_length=100)
    description: str | None = None
    price: float

    ingredients_links: list["ProductIngredientModel"] = Relationship(
        back_populates="product"
    )
