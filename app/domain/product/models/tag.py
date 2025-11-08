from sqlalchemy import Column, BigInteger, String, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import BaseEntity
from app.domain.product.enums.tag_type import TagType


class Tag(BaseEntity):
    __tablename__ = "tag"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    type = Column(Enum(TagType), nullable=False)

    product_tags = relationship("ProductTag", back_populates="tag_rel")
