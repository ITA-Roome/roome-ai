from app.db.base_repository import BaseRepository
from app.domain.product.models.product_tag import ProductTag
from sqlalchemy.orm import Session
from typing import List


class ProductTagRepository(BaseRepository[ProductTag]):
    def __init__(self):
        super().__init__(ProductTag)

    def find_by_product_id(self, db: Session, product_id: int) -> List[ProductTag]:
        return db.query(ProductTag).filter(ProductTag.product_id == product_id).all()

    def find_by_tag_id(self, db: Session, tag_id: int) -> List[ProductTag]:
        return db.query(ProductTag).filter(ProductTag.tag_id == tag_id).all()
