from sqlmodel import SQLModel, create_engine, Session
from src.infrastructure.models import (
    userModel,  # type: ignore
    productModel,  # type: ignore
    orderModel,  # type: ignore
    orderProductModel,  # type: ignore
    ingredientModel,  # type: ignore
    productIngredientModel,  # type: ignore
)
from dotenv import load_dotenv
import os


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)  # type: ignore


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session_database():
    with Session(engine) as session:
        yield session
