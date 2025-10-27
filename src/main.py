from fastapi import FastAPI
from src.infrastructure.db.db import init_db
from fastapi.middleware.cors import CORSMiddleware
from src.infrastructure.controllers.userController import router as user_router
from src.infrastructure.controllers.ingredientController import (
    router as ingredient_router,
)
from fastapi.openapi.utils import get_openapi
from typing import Any

app = FastAPI()

init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(ingredient_router)


def custom_openapi() -> dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema  # type: ignore

    openapi_schema = get_openapi(
        title="Burger POS System Backend",
        version="1.0.0",
        description="Backend API for Burger POS System",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema

    return app.openapi_schema  # type: ignore


app.openapi = custom_openapi
