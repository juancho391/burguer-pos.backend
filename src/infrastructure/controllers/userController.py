from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from src.application.dtos.userDto import CreateUserDto, UserDto, UserLoginDto
from src.application.services.userService import UserService
from src.domain.errors.errors import UserAlreadyExistsError, UserInvalidCredentialsError
from kink import di

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserDto)
def register(
    user: CreateUserDto, user_service: UserService = Depends(lambda: di[UserService])
) -> JSONResponse:
    try:
        user_created = user_service.create_user(new_user=user)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return JSONResponse(
        content=user_created.model_dump(), status_code=status.HTTP_201_CREATED
    )


@router.post("/token")
def login(
    user: UserLoginDto, user_service: UserService = Depends(lambda: di[UserService])
) -> JSONResponse:
    try:
        token = user_service.authenticate_user(user=user)
    except UserInvalidCredentialsError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    return JSONResponse(
        content={
            "message": "Login successful",
            "status": "success",
            "token": token.model_dump(),
        },
        status_code=status.HTTP_200_OK,
    )
