from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from src.application.dtos.ingredientDto import CreateIngredientDto, IngredientDto
from src.application.services.ingredientService import IngredientService
from kink import di


router = APIRouter(prefix="/ingredients", tags=["Ingredients"])


@router.post("/", response_model=IngredientDto)
def create_ingredient(
    ingredient: CreateIngredientDto,
    service: IngredientService = Depends(lambda: di[IngredientService]),
) -> JSONResponse:
    try:
        new_ingredient = service.create_ingredient(new_ingredient=ingredient)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return JSONResponse(
        content=new_ingredient.model_dump(), status_code=status.HTTP_201_CREATED
    )


@router.get("/", response_model=list[IngredientDto])
def get_all_ingredients(
    service: IngredientService = Depends(lambda: di[IngredientService]), limit: int = 10
) -> JSONResponse:
    ingredients = service.get_all_ingredients(limit=limit)
    return JSONResponse(
        content=[ingredient.model_dump() for ingredient in ingredients],
        status_code=status.HTTP_200_OK,
    )
