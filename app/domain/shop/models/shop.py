from sqlalchemy import Column, Integer, String
from app.db.base_class import BaseEntity


class Shop(BaseEntity):
    __tablename__ = "shop"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    # ---------- 메서드 ----------
    def update_name(self, name: str):
        """Shop 이름 수정"""
        self.name = name
