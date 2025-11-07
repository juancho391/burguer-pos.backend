from fastapi import APIRouter, Depends
from src.application.dtos.orderDto import CreateOrderDto, OrderWithProductsDto
from src.application.services.orderService import OrderService
from kink import di
from fastapi.responses import JSONResponse
import json


router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderWithProductsDto)
def create_order(
    order: CreateOrderDto, service: OrderService = Depends(lambda: di[OrderService])
) -> JSONResponse:
    order_created = service.create_order(order=order)
    return JSONResponse(
        content=json.loads(order_created.model_dump_json()), status_code=201
    )


@router.get("/", response_model=list[OrderWithProductsDto])
def get_all_orders(
    service: OrderService = Depends(lambda: di[OrderService]),
) -> JSONResponse:
    order_created = service.get_all_orders()
    return JSONResponse(
        content=json.loads(order_created.model_dump_json()), status_code=201
    )
