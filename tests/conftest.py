from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv
import pytest
import os

load_dotenv()

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

sqlite_url = f"sqlite:///db_test.db"

if TEST_DATABASE_URL:
    engine_test = create_engine(TEST_DATABASE_URL)


@pytest.fixture(autouse=True)
def clean_db():
    SQLModel.metadata.drop_all(engine_test)
    SQLModel.metadata.create_all(engine_test)
    yield


def get_session_test():
    with Session(engine_test) as session:
        yield session
