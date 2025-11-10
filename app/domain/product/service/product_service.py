from app.domain.product.repository.product_repository import ProductRepository
from app.domain.product.repository.product_tag_repository import ProductTagRepository
from app.domain.product.repository.tag_repository import TagRepository
from app.domain.product.models.product import Product
from app.domain.ai.dto.request.recommend_products_request import (
    RecommendProductsRequest,
)
from sqlalchemy.orm import Session
from typing import List


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.product_tag_repository = ProductTagRepository()
        self.tag_repository = TagRepository()

    def get_product(self, product_id: int) -> Product | None:
        return self.product_repository.find_by_id(product_id)

    def get_products_search_with_or_conditions(
        self, db: Session, filters: RecommendProductsRequest
    ) -> List[Product]:
        return self.product_repository.find_with_or_conditions(db, filters)
