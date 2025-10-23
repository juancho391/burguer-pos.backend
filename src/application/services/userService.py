from src.domain.repositories.userRepository import IUserRepository
from src.application.dtos.userDto import CreateUserDto, UserDto, UserLoginDto
from src.application.dtos.tokenDto import TokenDto
from src.domain.classes.user import User
from kink import inject  # type: ignore
from src.domain.errors.errors import UserAlreadyExistsError, UserInvalidCredentialsError
from src.infrastructure.security.hasher import PasswordHasher
from src.infrastructure.security.auth import JwtService
from src.domain.classes.token import Token


@inject  # type: ignore
class UserService:
    def __init__(
        self, user_repository: IUserRepository, jwt_service: JwtService
    ) -> None:
        self.repository = user_repository
        self.auth_service = jwt_service

    def create_user(self, new_user: CreateUserDto) -> UserDto:
        existing_user = self.repository.get_user_by_email(email=new_user.email)
        if existing_user:
            raise UserAlreadyExistsError(email=new_user.email)

        new_user.password = PasswordHasher.hash_password(new_user.password)
        user_entity = User.create_new_one(
            name=new_user.name, email=new_user.email, password=new_user.password
        )
        user_created = self.repository.add_user(user_entity)
        return UserDto(**user_created.__dict__)

    def authenticate_user(self, user: UserLoginDto) -> TokenDto:
        user_in_db = self.repository.get_user_by_email(email=user.email)
        if not user_in_db or not PasswordHasher.verify_password(
            user.password, user_in_db.password
        ):
            raise UserInvalidCredentialsError()
        return TokenDto(**self.auth_service.create_access_token(user_in_db.id, user.email).__dict__)  # type: ignore

    def get_current_user(self, token: Token) -> TokenDto:
        return TokenDto(**self.auth_service.verify_token(token).__dict__)
