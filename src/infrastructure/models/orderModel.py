from sqlmodel import Field, SQLModel  # pyright: ignore[reportUnknownVariableType]
from datetime import datetime, timezone


class OrderModel(SQLModel, table=True):
    __tablename__ = "Orders"  # type: ignore
    id: int = Field(default=None, primary_key=True)
    id_user: int = Field(foreign_key="Users.id", nullable=False)
    total_price: int = Field(nullable=False)
    customer_name: str = Field(nullable=False, max_length=100)
    service_price: int = Field(default=0)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
