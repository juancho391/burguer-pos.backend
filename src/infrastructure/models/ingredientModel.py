from sqlmodel import Field, SQLModel  # pyright: ignore[reportUnknownVariableType]


class IngredientModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    stock: int | None = 0
    reposition_point: int
