from app.domain.shop.models.shop import Shop
from app.db.base_repository import BaseRepository


class ShopRepository(BaseRepository[Shop]):
    def __init__(self):
        super().__init__(Shop)

    def find_by_name(self, db, name: str) -> Shop | None:
        return db.query(Shop).filter(Shop.name == name).first()

    def find_by_id(self, db, shop_id: int) -> Shop | None:
        return db.query(Shop).filter(Shop.id == shop_id).first()
