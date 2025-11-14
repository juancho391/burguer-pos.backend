from sqlmodel import (
    Field,  # pyright: ignore[reportUnknownVariableType]
    SQLModel,
    Relationship,
)


class ProductIngredientModel(SQLModel, table=True):
    __tablename__ = "ProductIngredients"

    id_product: int = Field(foreign_key="Products.id", nullable=False, primary_key=True)
    id_ingredient: int = Field(
        foreign_key="Ingredients.id", nullable=False, primary_key=True
    )
    quantity: int

    product: "ProductModel" = Relationship(back_populates="ingredients_links")  # type: ignore # noqa: F821
    ingredient: "IngredientModel" = Relationship(back_populates="products_links")  # type: ignore # noqa: F821
