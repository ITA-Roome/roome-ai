from app.db.base_repository import BaseRepository
from app.domain.product.models.tag import Tag
from sqlalchemy.orm import Session
from typing import Optional, List
from app.domain.product.enums.tag_type import TagType


class TagRepository(BaseRepository[Tag]):
    def __init__(self):
        super().__init__(Tag)

    def find_by_type(self, db: Session, tag_type: str) -> List[Tag]:
        return db.query(Tag).filter(Tag.type == tag_type).all()

    def find_by_name(self, db: Session, name: str) -> Optional[Tag]:
        return db.query(Tag).filter(Tag.name == name).first()
