from app.db.base_repository import BaseRepository
from app.domain.product.models.product import Product
from sqlalchemy.orm import Session
from typing import Optional, List
from app.domain.product.enums.category import Category
from app.domain.product.enums.color import Color


class ProductRepository(BaseRepository[Product]):
    def __init__(self):
        super().__init__(Product)

    def find_by_category(self, db: Session, category: Category) -> List[Product]:
        return db.query(Product).filter(Product.category == category).all()

    def find_by_color(self, db: Session, color: Color) -> List[Product]:
        return db.query(Product).filter(Product.color == color).all()
