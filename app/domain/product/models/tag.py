from sqlalchemy import Column, Integer, String, Enum
from app.db.base_class import BaseEntity
from enum import Enum as PyEnum


class TagType(str, PyEnum):
    COLOR = "COLOR"
    MATERIAL = "MATERIAL"
    FEATURE = "FEATURE"
    PRODUCT_TYPE = "PRODUCT_TYPE"
    SIZE = "SIZE"
    USAGE = "USAGE"
    STYLE = "STYLE"
    MOOD = "MOOD"


class Tag(BaseEntity):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    type = Column(Enum(TagType), nullable=False)
