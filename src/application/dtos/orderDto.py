from sqlmodel import SQLModel
from src.application.dtos.productDto import ProductOrderDto, ProductDtoResponse
from datetime import datetime
from typing import Optional


class CreateOrderDto(SQLModel):
    customer_name: str
    products: list[ProductOrderDto]
    include_service: bool


class CreateOrderDbDto(SQLModel):
    id_user: int
    total_price: int
    customer_name: str
    service_price: int
    created_at: Optional[datetime]


class OrderDto(CreateOrderDbDto):
    id: int


class OrderWithProductsDto(OrderDto):
    products: list[ProductDtoResponse]
