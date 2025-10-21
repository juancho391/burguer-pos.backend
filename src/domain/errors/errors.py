# src/domain/errors.py


class DomainError(Exception):
    pass


class UserAlreadyExistsError(DomainError):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"A user with the email '{email}' already exists.")
