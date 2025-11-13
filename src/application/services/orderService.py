from kink import inject
from src.application.dtos.orderDto import CreateOrderDto, OrderWithProductsDto
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

    def create_order(self, order: CreateOrderDto) -> OrderWithProductsDto:
        products_db = []
        for product in order.products:
            product_db = self.product_repository.get_product_by_id(product.id)
            if not product_db:
                raise ProductNotFoundError(id=product.id)
            for _ in range(product.quantity):
                products_db.append(product_db)

        new_order = Order.create_new_one(
            id_user=1,
            customer_name=order.customer_name,
            products=products_db,
            include_service=order.include_service,
        )

        order_created = self.order_repossitory.create_order(new_order)

        product_quantities = {}
        for product in products_db:
            if product.name in product_quantities:
                product_quantities[product.name] += 1
            else:
                product_quantities[product.name] = 1
        order_products = []
        order_prducts_ids = []
        for product in products_db:
            if product.id not in order_prducts_ids:
                order_products.append(
                    OrderProduct.create_new_one(
                        quantity=product_quantities[product.name],
                        unit_price=product.price,
                        product_id=product.id,
                        order_id=order_created.id,
                    )
                )
                order_prducts_ids.append(product.id)

        relations_created = self.order_product_repository.create_all_order_product(
            order_products=order_products
        )
        print("order and relations created successfully")
        if not relations_created:
            raise Exception("Error creating order products")
        return OrderWithProductsDto(**order_created.__dict__)

    def get_all_orders(self):
        orders = self.order_repossitory.get_all_orders()
        return orders
