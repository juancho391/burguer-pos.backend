from src.domain.repositories.orderProductRepository import IOrderProductRepository
from sqlmodel import Session
from src.domain.classes.orderProduct import OrderProduct
from src.application.dtos.orderProductDto import CreateOrderProductDto
from src.infrastructure.models.orderProductModel import OrderProductModel


class PostgreSqlOrderProductRepository(IOrderProductRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_all_order_product(self, order_products: list[OrderProduct]) -> bool:

        order_products_model = [
            OrderProductModel.model_validate(
                CreateOrderProductDto(
                    id_order=order_product.order_id,
                    id_product=order_product.product_id,
                    quantity=order_product.quantity,
                    unit_price=order_product.unit_price,
                )
            )
            for order_product in order_products
        ]

        self.session.add_all(order_products_model)
        self.session.commit()
        return True

    def add_product_to_order(self, order_product: OrderProduct) -> bool:
        order_product_model = OrderProductModel.model_validate(
            CreateOrderProductDto(
                id_order=order_product.order_id,
                id_product=order_product.product_id,
                quantity=order_product.quantity,
                unit_price=order_product.unit_price,
            )
        )
        self.session.add(order_product_model)
        self.session.commit()
        self.session.refresh(order_product_model)
        if not order_product_model.id:
            return False
        return True
