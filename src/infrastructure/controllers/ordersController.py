from fastapi import APIRouter, Depends, HTTPException, status
from src.application.dtos.orderDto import CreateOrderDto, OrderWithProductsDto
from src.application.dtos.productDto import ProductOrderDto
from src.application.services.orderService import OrderService
from kink import di
from fastapi.responses import JSONResponse
import json
from src.domain.errors.errors import OrderNotFoundError, ProductNotFoundError


router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/")
def create_order(
    order: CreateOrderDto, service: OrderService = Depends(lambda: di[OrderService])
) -> JSONResponse:
    order_created = service.create_order(order=order)
    return JSONResponse(
        content=json.loads(order_created.model_dump_json()), status_code=201
    )


@router.post("/{order_id}")
def add_products_to_order(
    product: ProductOrderDto,
    order_id: int,
    service: OrderService = Depends(lambda: di[OrderService]),
) -> JSONResponse:
    try:
        productd_added = service.add_product_to_order(
            order_id=order_id, product=product
        )
        status_request = "Success" if productd_added else "Failed"
    except OrderNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ProductNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    return JSONResponse(content=f"Products added {status_request}", status_code=201)


@router.get("/", response_model=list[OrderWithProductsDto])
def get_all_orders(
    service: OrderService = Depends(lambda: di[OrderService]),
) -> JSONResponse:
    order_created = service.get_all_orders()
    return JSONResponse(
        content=json.loads(order_created.model_dump_json()), status_code=201
    )
