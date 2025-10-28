from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from kink import di
from src.application.dtos.productDto import CreateProductDto, ProductDto
from src.application.services.productService import ProductService


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
