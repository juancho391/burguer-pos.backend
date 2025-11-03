# src/domain/errors.py


class DomainError(Exception):
    pass


class UserAlreadyExistsError(DomainError):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"A user with the email '{email}' already exists.")


class UserInvalidCredentialsError(DomainError):
    def __init__(self):
        super().__init__("Invalid email or password.")


class AuthenticationError(DomainError):
    def __init__(self, message: str = "Authentication failed."):
        super().__init__(message)


class PriceZeroError(DomainError):
    def __init__(self, message: str = "Price must be greater than zero."):
        super().__init__(message)


class IngredientNotFoundError(DomainError):
    def __init__(self, id: int):
        super().__init__(f"Ingredient with id :{id} not found.")


class ProductNotFoundError(DomainError):
    def __init__(self, id: int):
        super().__init__(f"Product with id :{id} not found.")
