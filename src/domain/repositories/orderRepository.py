from abc import abstractmethod, ABC
from src.domain.classes.order import Order


class IOrderRepository(ABC):

    @abstractmethod
    def create_order(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get_order_by_id(self, id: int) -> Order:
        pass

    @abstractmethod
    def get_all_orders(self) -> list[Order]:
        pass
