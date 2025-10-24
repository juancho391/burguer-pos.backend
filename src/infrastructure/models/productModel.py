from sqlmodel import Field, SQLModel  # pyright: ignore[reportUnknownVariableType]


class ProductModel(SQLModel, table=True):
    __tablename__ = "Products"  # type: ignore
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, max_length=100)
    description: str | None = None
    price: float
