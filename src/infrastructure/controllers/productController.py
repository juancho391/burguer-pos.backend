from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from kink import di
from src.application.dtos.productDto import (
    CreateProductDto,
    ProductDto,
)
from src.application.services.productService import ProductService
from src.domain.errors.errors import ProductNotFoundError


router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductDto)
def create_product(
    product: CreateProductDto,
    service: ProductService = Depends(lambda: di[ProductService]),
):
    try:
        new_product = service.create_product(product)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return JSONResponse(
        content=new_product.model_dump(), status_code=status.HTTP_201_CREATED
    )


@router.get("/", response_model=list[ProductDto])
def get_all_products(
    service: ProductService = Depends(lambda: di[ProductService]), limit: int = 10
) -> list[ProductDto]:
    products = service.get_all_products(limit=limit)
    return JSONResponse(
        content=[product.model_dump() for product in products],
        status_code=status.HTTP_200_OK,
    )


@router.delete("/")
def delete_product(
    id: int, service: ProductService = Depends(lambda: di[ProductService])
):
    try:
        service.delete_product(id=id)
    except ProductNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return JSONResponse(
        content={"message": "Product deleted successfully"},
        status_code=status.HTTP_200_OK,
    )
