from src.domain.repositories.orderRepository import IOrderRepository
from sqlmodel import Session, select
from src.domain.classes.order import Order
from src.infrastructure.models.orderModel import OrderModel
from src.application.dtos.orderDto import CreateOrderDbDto


class PostgreSqlOrderRepository(IOrderRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_order(self, order: Order) -> Order:

        order_model = OrderModel.model_validate(
            CreateOrderDbDto(
                id_user=order.id_user,
                customer_name=order.customer_name,
                service_price=order.service_price,
                total_price=order.total_price,
                created_at=order.created_at,
            )
        )
        self.session.add(order_model)
        self.session.commit()
        self.session.refresh(order_model)
        return Order.create_from_db(
            id=order_model.id,
            id_user=order_model.id_user,
            customer_name=order_model.customer_name,
            created_at=order_model.created_at,
            total_price=order_model.total_price,
            service_price=order_model.service_price,
            products=order.products,
        )

    def get_order_by_id(self, id: int) -> Order:
        pass

    def get_all_orders(self, limit: int) -> list[Order]:
        orders = self.session.exec(select(OrderModel).limit(limit=limit)).all()
        print(orders)
