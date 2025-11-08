from sqlalchemy import Column, Integer, String, Enum
from app.db.base_class import BaseEntity
from app.domain.product.enums.tag_type import TagType


class Tag(BaseEntity):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    type = Column(Enum(TagType), nullable=False)
