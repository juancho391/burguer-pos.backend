from src.domain.classes.user import User
from src.domain.repositories.userRepository import IUserRepository
from sqlmodel import Session, select
from src.infrastructure.models.userModel import UserModel
from src.application.dtos.userDto import CreateUserDto


class PostgreSqlUserRepository(IUserRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def add_user(self, user: User) -> User:
        user_model = UserModel.model_validate(CreateUserDto(**user.__dict__))
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)
        return User.create_from_db(**user_model.model_dump())

    def get_user_by_email(self, email: str) -> User | None:
        user_model = self.session.exec(
            select(UserModel).where(UserModel.email == email)
        ).first()
        if user_model:
            return User.create_from_db(**user_model.model_dump())
        return None
