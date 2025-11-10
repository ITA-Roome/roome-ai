from pydantic import BaseModel, Field
from app.domain.product.enums.category import Category
from app.domain.product.enums.color import Color
from app.domain.product.enums.tag_type import TagType
from typing import Optional


class RecommendProductsRequest(BaseModel):
    """사용자 입력 기반 추천 요청"""

    user_id: int
    color: Optional[Color] = Field(None, description="상품 색상 (예: BEIGE, WHITE 등)")
    price: Optional[int] = Field(None, description="상품 가격대 (예: 50000)")
    tag_type: Optional[TagType] = Field(
        None, description="상품 태그 타입 (예: COZY, MODERN 등)"
    )
    category: Optional[Category] = Field(
        None, description="상품 카테고리 (예: BEDROOM_BED 등)"
    )
