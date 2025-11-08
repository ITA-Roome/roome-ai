from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import BaseEntity


class ProductTag(BaseEntity):
    __tablename__ = "product_tag"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(
        Integer, ForeignKey("product.id", ondelete="CASCADE"), nullable=False
    )
    tag_id = Column(Integer, ForeignKey("tag.id", ondelete="CASCADE"), nullable=False)

    product = relationship("Product", back_populates="product_tags")
    tag = relationship("Tag")
