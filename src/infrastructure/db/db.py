from sqlmodel import SQLModel, create_engine, Session
from src.infrastructure.models import (
    userModel,  # type: ignore # noqa: F401
    productModel,  # type: ignore # noqa: F401
    orderModel,  # type: ignore # noqa: F401
    orderProductModel,  # type: ignore # noqa: F401
    ingredientModel,  # type: ignore # noqa: F401
    productIngredientModel,  # type: ignore # noqa: F401
)
from dotenv import load_dotenv
import os


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL_DEV = os.getenv("DATABASE_URL_DEV")

engine = create_engine(DATABASE_URL_DEV)  # type: ignore


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session_database():
    with Session(engine) as session:
        yield session
