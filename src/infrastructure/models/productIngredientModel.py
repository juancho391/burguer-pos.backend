from sqlmodel import Field, SQLModel  # pyright: ignore[reportUnknownVariableType]


class ProductIngredientModel(SQLModel, table=True):
    __tablename__ = "ProductIngredients"  # type: ignore
    id: int = Field(default=None, primary_key=True)
    id_product: int = Field(foreign_key="Products.id", nullable=False)
    id_ingredient: int = Field(foreign_key="Ingredients.id", nullable=False)
    quantity: int
