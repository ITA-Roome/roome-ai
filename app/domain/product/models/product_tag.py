from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import BaseEntity


class ProductTag(BaseEntity):
    __tablename__ = "product_tag"

    id = Column(BigInteger, primary_key=True, index=True)
    product = Column(
        BigInteger, ForeignKey("product.id", ondelete="CASCADE"), nullable=False
    )
    tag = Column(BigInteger, ForeignKey("tag.id", ondelete="CASCADE"), nullable=False)

    # 관계 정의 (DDL 컬럼명과 충돌 피하기 위해 rel suffix 사용)
    product_rel = relationship("Product", back_populates="product_tags")
    tag_rel = relationship("Tag", back_populates="product_tags")
