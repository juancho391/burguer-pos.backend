from kink import inject
from src.application.dtos.orderDto import (
    CreateOrderDto,
    OrderWithProductsDto,
    OrderDto,
    OrderWithProductsNoIngredientsDto,
)
from src.application.dtos.productDto import ProductOrderDto
from src.domain.classes.order import Order
from src.domain.repositories.productRepository import IProductRepository
from src.domain.errors.errors import ProductNotFoundError, OrderNotFoundError
from src.domain.repositories.orderRepository import IOrderRepository
from src.domain.classes.orderProduct import OrderProduct
from src.domain.repositories.orderProductRepository import IOrderProductRepository


@inject
class OrderService:
    def __init__(
        self,
        product_repository: IProductRepository,
        order_repository: IOrderRepository,
        order_product_repository: IOrderProductRepository,
    ):
        self.product_repository = product_repository
        self.order_repository = order_repository
        self.order_product_repository = order_product_repository

    def create_order(self, order: CreateOrderDto) -> OrderDto:
        new_order = Order.create_new_one(
            id_user=1,
            customer_name=order.customer_name,
        )
        order_created = self.order_repository.create_order(new_order)
        return OrderDto(**order_created.__dict__)

    def add_product_to_order(self, order_id: int, product: ProductOrderDto):
        order_db = self.order_repository.get_order_by_id(order_id)
        if not order_db:
            raise OrderNotFoundError(order_id)
        product_db = self.product_repository.get_product_by_id(product.id)
        if not product_db:
            raise ProductNotFoundError(product.id)

        order_product = OrderProduct.create_new_one(
            order_id=order_db.id,
            product_id=product.id,
            quantity=product.quantity,
            unit_price=product_db.price,
        )
        order_product_saved = self.order_product_repository.add_product_to_order(
            order_product=order_product
        )
        return True if order_product_saved else False

    def get_all_orders(self, limit: int) -> list[OrderWithProductsDto] | None:
        orders = self.order_repository.get_all_orders(limit=limit)
        if not orders:
            return []
        return [
            OrderWithProductsNoIngredientsDto(
                id=order.id,
                customer_name=order.customer_name,
                products=order.products,
                total_price=order.total_price,
                service_price=order.service_price,
                created_at=order.created_at,
                id_user=order.id_user,
            )
            for order in orders
        ]
