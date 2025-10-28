from src.domain.repositories.productRepository import IProductRepository
from sqlmodel import Session
from src.infrastructure.models.productModel import ProductModel
from src.infrastructure.models.ingredientModel import IngredientModel
from src.domain.classes.product import Product
from src.application.dtos.productDto import CreateProductDto
from src.infrastructure.models.productIngredientModel import ProductIngredientModel


class PostgreSqlProductRepository(IProductRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_product(self, product: Product) -> Product:
        new_product = ProductModel.model_validate(CreateProductDto(**product.__dict__))
        self.session.add(new_product)
        self.session.commit()
        self.session.refresh(new_product)
        return Product.create_from_db(
            id=new_product.id,
            name=new_product.name,
            description=new_product.description,
            price=new_product.price,
            ingredients=product.ingredients,
        )
