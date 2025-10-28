from sqlmodel import SQLModel


class ProductIngredientDto(SQLModel):
    id_product: int
    id_ingredient: int
    quantity: int
