from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from src.application.dtos.userDto import CreateUserDto, UserDto
from src.application.services.userService import UserService
from src.domain.errors.errors import UserAlreadyExistsError
from kink import di

router = APIRouter()


@router.post("/users", response_model=UserDto)
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
