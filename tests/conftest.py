from sqlmodel import create_engine, SQLModel, Session
import pytest

sqlite_name = "db_test.db"
sqlite_url = f"sqlite:///{sqlite_name}"


engine_test = create_engine(sqlite_url)


@pytest.fixture(autouse=True)
def clean_db():
    SQLModel.metadata.drop_all(engine_test)
    SQLModel.metadata.create_all(engine_test)
    yield


def get_session_test():
    with Session(engine_test) as session:
        yield session
