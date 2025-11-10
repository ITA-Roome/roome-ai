from app.db.base_repository import BaseRepository
from app.domain.product.models.product import Product
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from typing import List
from app.domain.product.enums.category import Category
from app.domain.product.enums.color import Color
from app.domain.ai.dto.request.recommend_products_request import (
    RecommendProductsRequest,
)


class ProductRepository(BaseRepository[Product]):
    def __init__(self):
        super().__init__(Product)

    def find_by_id(self, db: Session, product_id) -> Product | None:
        return db.query(Product).filter(Product.id == product_id).first()

    def find_by_category(self, db: Session, category: Category) -> List[Product]:
        return db.query(Product).filter(Product.category == category).all()

    def find_by_color(self, db: Session, color: Color) -> List[Product]:
        return db.query(Product).filter(Product.color == color).all()

    def find_with_or_conditions(
        self, db: Session, filters: RecommendProductsRequest
    ) -> List[Product]:
        """
        사용자의 입력 조건(color, category, price, tag_type)을 기반으로
        OR 조건으로 상품을 검색 (중복 제거)
        """

        query = db.query(Product)
        conditions = []

        color = filters.color
        category = filters.category
        price = filters.price
        tag_type = filters.tag_type

        # 색상 필터
        if color:
            conditions.append(Product.color == color)

        # 카테고리 필터
        if category:
            conditions.append(Product.category == category)

        # 가격대 필터 (±10%)
        if price:
            try:
                price = int(price)
                min_price = int(price * 0.9)
                max_price = int(price * 1.1)
                conditions.append(
                    and_(Product.price >= min_price, Product.price <= max_price)
                )
            except ValueError:
                pass

        # 태그 타입 필터
        if tag_type:
            from app.domain.product.models.product_tag import ProductTag
            from app.domain.product.models.tag import Tag

            query = query.join(ProductTag, ProductTag.product == Product.id).join(
                Tag, ProductTag.tag == Tag.id
            )
            conditions.append(Tag.type == tag_type)

        # 조건 결합 (OR)
        if conditions:
            query = query.filter(or_(*conditions))

        # 중복 제거 및 제한
        query = query.distinct(Product.id).limit(200)

        return query.all()
