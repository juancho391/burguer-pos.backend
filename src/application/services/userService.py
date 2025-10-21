from src.domain.repositories.userRepository import IUserRepository
from src.application.dtos.userDto import CreateUserDto, UserDto
from src.domain.classes.user import User
from kink import inject  # type: ignore
from src.domain.errors.errors import UserAlreadyExistsError


@inject  # type: ignore
class UserService:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.repository = user_repository

    def create_user(self, new_user: CreateUserDto) -> UserDto:
        existing_user = self.repository.get_user_by_email(email=new_user.email)
        if existing_user:
            raise UserAlreadyExistsError(email=new_user.email)

        user_entity = User.create_new_one(
            name=new_user.name, email=new_user.email, password=new_user.password
        )
        user_created = self.repository.add_user(user_entity)
        return UserDto(**user_created.__dict__)
