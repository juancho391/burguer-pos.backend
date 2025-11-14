from sqlmodel import SQLModel
from src.application.dtos.productDto import ProductDtoResponse, ProductNoIngredientsDto
from datetime import datetime


# Dto for validating order creation request
class CreateOrderDto(SQLModel):
    customer_name: str
    include_service: bool


# Dto for validating order creation in db
class CreateOrderDbDto(SQLModel):
    id_user: int
    total_price: int
    customer_name: str
    service_price: int
    created_at: datetime


# Dto for validating order response in creating order request
class OrderDto(CreateOrderDbDto):
    id: int


# Dto for validating order response with products
class OrderWithProductsDto(OrderDto):
    products: list[ProductDtoResponse]


# Dto for validating order response with products without ingredients
class OrderWithProductsNoIngredientsDto(OrderDto):
    products: list[ProductNoIngredientsDto]
