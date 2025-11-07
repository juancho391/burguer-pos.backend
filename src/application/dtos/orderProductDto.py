from sqlmodel import SQLModel


class CreateOrderProductDto(SQLModel):
    id_order: int
    id_product: int
    quantity: int
    unit_price: int


class OrderProductDbDto(CreateOrderProductDto):
    id: int
