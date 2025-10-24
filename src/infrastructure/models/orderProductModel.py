from sqlmodel import SQLModel, Field  # pyright: ignore[reportUnknownVariableType]


class OrderProductModel(SQLModel, table=True):
    __tablename__ = "OrderProducts"  # type: ignore
    id: int = Field(default=None, primary_key=True)
    id_order: int = Field(foreign_key="Orders.id", nullable=False)
    id_product: int = Field(foreign_key="Products.id", nullable=False)
    quantity: int = Field(nullable=False)
    unit_price: int = Field(nullable=False)
