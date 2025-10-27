from src.domain.repositories.productRepository import IProductRepository
from sqlmodel import Session
from src.infrastructure.models.productModel import ProductModel
from src.domain.classes.product import Product
from src.application.dtos.productDto import CreateProductDto


class PostgreSqlProductRepository(IProductRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_product(self, product: Product) -> Product:
        product_model = ProductModel.model_validate(
            CreateProductDto(**product.__dict__)
        )
        self.session.add(product_model)
        self.session.commit()
        self.session.refresh(product_model)
        return Product.create_from_db(**product_model.model_dump())
