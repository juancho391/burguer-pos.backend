from sqlmodel import (
    Field,  # pyright: ignore[reportUnknownVariableType]
    SQLModel,
    Relationship,
)


class ProductIngredientModel(SQLModel, table=True):
    __tablename__ = "ProductIngredients"

    id: int = Field(default=None, primary_key=True)
    id_product: int = Field(foreign_key="Products.id", nullable=False)
    id_ingredient: int = Field(foreign_key="Ingredients.id", nullable=False)
    quantity: int

    product: "ProductModel" = Relationship(back_populates="ingredients_links")  # type: ignore # noqa: F821
    ingredient: "IngredientModel" = Relationship(back_populates="products_links")  # type: ignore # noqa: F821
