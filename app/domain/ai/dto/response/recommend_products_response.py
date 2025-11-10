from pydantic import BaseModel, Field
from typing import Optional, List
from app.domain.product.enums.category import Category
from app.domain.product.enums.color import Color


class AIRecommendedProduct(BaseModel):
    """AI가 추천한 상품 DTO"""

    id: int
    name: Optional[str]
    category: Optional[Category]
    color: Optional[Color]
    price: Optional[int]
    tags: Optional[List[str]] = Field(default_factory=list)

    class Config:
        from_attributes = True


class AIRecommendResponse(BaseModel):
    """AI 추천 응답"""

    user_description: str = Field(..., description="AI가 분석한 사용자 온보딩 요약")
    recommended_products: List[AIRecommendedProduct] = Field(
        ..., description="AI가 추천한 상품 리스트"
    )
    ai_comment: str = Field(..., description="AI 추천에 대한 한줄 설명")

    class Config:
        from_attributes = True
