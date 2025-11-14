from __future__ import annotations

from sqlmodel import (
    SQLModel,
    Field,  # pyright: ignore[reportUnknownVariableType]
    Relationship,
)  # pyright: ignore[reportUnknownVariableType]


class OrderProductModel(SQLModel, table=True):
    __tablename__ = "OrderProducts"  # type: ignore
    id_order: int = Field(foreign_key="Orders.id", nullable=False, primary_key=True)
    id_product: int = Field(foreign_key="Products.id", nullable=False, primary_key=True)
    quantity: int = Field(nullable=False)
    unit_price: int = Field(nullable=False)

    orders: list["OrderModel"] = Relationship(back_populates="product_links")  # type: ignore # noqa: F821
    product: "ProductModel" = Relationship(back_populates="order_links")  # type: ignore # noqa: F821
