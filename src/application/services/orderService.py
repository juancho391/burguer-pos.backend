from kink import inject
from src.application.dtos.orderDto import (
    CreateOrderDto,
    OrderWithProductsDto,
    CreateOrderDbDto,
    OrderDto,
)
from src.domain.classes.order import Order
from src.domain.repositories.productRepository import IProductRepository
from src.domain.errors.errors import ProductNotFoundError
from src.domain.repositories.orderRepository import IOrderRepository
from src.domain.classes.orderProduct import OrderProduct
from src.domain.repositories.orderProductRepository import IOrderProductRepository


@inject
class OrderService:
    def __init__(
        self,
        product_repository: IProductRepository,
        order_repossitory: IOrderRepository,
        order_product_repository: IOrderProductRepository,
    ):
        self.product_repository = product_repository
        self.order_repossitory = order_repossitory
        self.order_product_repository = order_product_repository

    def create_order(self, order: CreateOrderDto) -> OrderDto:
        new_order = Order.create_new_one(
            id_user=1,
            customer_name=order.customer_name,
        )
        order_created = self.order_repossitory.create_order(new_order)
        return OrderDto(**order_created.__dict__)

    def get_all_orders(self):
        orders = self.order_repossitory.get_all_orders()
        return orders
