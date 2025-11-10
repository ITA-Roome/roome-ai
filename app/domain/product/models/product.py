from sqlalchemy import Column, BigInteger, String, Integer, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import BaseEntity
from app.domain.product.enums.category import Category
from app.domain.product.enums.color import Color


class Product(BaseEntity):
    __tablename__ = "product"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=True)
    category = Column(Enum(Category), nullable=False)
    color = Column(Enum(Color), nullable=False)

    product_tags = relationship(
        "ProductTag", back_populates="product_rel", cascade="all, delete-orphan"
    )
