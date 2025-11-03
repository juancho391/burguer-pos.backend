from src.domain.repositories.productRepository import IProductRepository
from sqlmodel import Session
from src.infrastructure.models.productModel import ProductModel
from src.domain.classes.product import Product
from src.application.dtos.productDto import CreateProductDto
from sqlmodel import select, delete


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

    def get_all_products(self, limit: int) -> list[Product]:
        products = self.session.exec(select(ProductModel).limit(limit=limit)).all()
        return [
            Product.create_from_db_with_ingredients(
                id=product.id,
                name=product.name,
                description=product.description,
                price=product.price,
                ingredients=product.ingredients_links,
            )
            for product in products
        ]

    def get_product_by_id(self, id: int) -> Product | None:
        product = self.session.get(ProductModel, id)
        if not product:
            return None
        return Product.create_from_db_with_ingredients(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            ingredients=product.ingredients_links,
        )

    def delete_product(self, id: int) -> bool:
        result = self.session.exec(delete(ProductModel).where(ProductModel.id == id))
        self.session.commit()
        return result.rowcount > 0
