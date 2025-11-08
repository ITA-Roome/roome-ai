from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.ai.service.ai_service import AIService
from app.domain.ai.dto.response.recommend_products_response import AIRecommendResponse
from app.domain.ai.dto.request.recommend_products_request import (
    RecommendProductsRequest,
)

router = APIRouter(
    prefix="/ai",
    tags=["AI 추천 시스템 "],
    responses={
        404: {"description": "User not found"},
        500: {"description": "Internal Server Error"},
    },
)

ai_service = AIService()


@router.post(
    "/recommend/products",
    response_model=AIRecommendResponse,
    summary="AI 기반 상품 추천",
    description="""
    💡 **AI Recommendation Endpoint**

    사용자 온보딩 정보와 입력된 필터(color, category, price, tag_type)를 바탕으로  
    OpenAI 모델이 가장 어울리는 상품을 50개 이내로 추천합니다.

    ---
    **추천 로직 요약**
    1. `user_id`로 유저 온보딩 정보 조회  
    2. 입력 필터(color, price, category, tag_type)로 OR 조건 검색  
    3. GPT 모델이 온보딩/입력 조건 기반 가중치 계산  
    4. 최종 추천 상품 ID를 반환  

    ---
    ⚙️ **가중치**
    - 온보딩 일치율: 0.7  
    - 사용자 입력 조건 일치율: 0.2  
    - 스타일 다양성: 0.1  
    """,
)
def recommend_products(
    request: RecommendProductsRequest,
    db: Session = Depends(get_db),
):
    """
    사용자 온보딩 + 입력 조건 기반 상품 추천 API
    """
    try:
        result = ai_service.recommend_for_user(db, request.user_id, request)
        return result

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )

    except Exception as e:
        print(f" AI Recommendation Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="AI 추천 처리 중 오류가 발생했습니다.",
        )
