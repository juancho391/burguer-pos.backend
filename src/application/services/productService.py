from src.domain.repositories.productRepository import IProductRepository
from src.domain.repositories.productIngredientRepository import (
    IProductIngredientRepository,
)
from src.domain.repositories.ingredientRepository import IIngredientRepository
from src.application.dtos.productDto import CreateProductDto, ProductDto
from src.domain.classes.product import Product
from src.domain.classes.productIngredient import ProductIngredient
from src.domain.classes.ingredient import Ingredient
from kink import di, inject
from src.domain.errors.errors import IngredientNotFoundError


@inject
class ProductService:
    def __init__(
        self,
        productRepository: IProductRepository,
        productIngredientRepository: IProductIngredientRepository,
        ingredientRepository: IIngredientRepository,
    ) -> None:
        self.productRepository = productRepository
        self.productIngredientRepository = productIngredientRepository
        self.ingredientRepository = ingredientRepository

    def create_product(self, product: CreateProductDto):
        for ingredient in product.ingredients:
            ingredient_db = self.ingredientRepository.get_ingredient_by_id(
                ingredient.id
            )
            if not ingredient_db:
                raise IngredientNotFoundError(ingredient.id)

        new_product = Product.create_new_one(
            name=product.name,
            description=product.description,
            price=product.price,
            ingredients=product.ingredients,
        )
        product_created = self.productRepository.create_product(new_product)
        product_ingredients = [
            ProductIngredient.create_new_one(
                id_product=product_created.id,
                id_ingredient=ingredient.id,
                quantity=ingredient.quantity,
            )
            for ingredient in new_product.ingredients
        ]
        relations_created = (
            self.productIngredientRepository.create_all_product_ingredients(
                product_ingredients
            )
        )
        if not relations_created:
            raise Exception("Error creating product ingredients")
        return ProductDto(**product_created.__dict__)
