from app.core.openai_client import generate_text
from app.domain.user.service.user_service import UserService
from app.domain.product.service.product_service import ProductService
from app.domain.ai.dto.request.recommend_products_request import (
    RecommendProductsRequest,
)
from app.domain.ai.dto.response.recommend_products_response import (
    AIRecommendResponse,
    AIRecommendedProduct,
)
from sqlalchemy.orm import Session
import json


class AIService:
    def __init__(self):
        self.user_service = UserService()
        self.product_service = ProductService()

    def recommend_products_for_user(
        self, db: Session, user_id: int, filters: RecommendProductsRequest
    ) -> AIRecommendResponse:
        """
        온보딩 중심(0.7) + 사용자 입력 조건(0.2) + 다양성(0.1)
        프롬프트 기반 추천 시스템 (가격 ±20% 허용)
        """

        # 온보딩 조회
        user_data = self.user_service.get_user_onboarding(db, user_id)
        if not user_data:
            raise ValueError("User onboarding not found")

        # 상품 후보 조회
        candidates = self.product_service.get_products_search_with_or_conditions(
            db, filters
        )
        if not candidates:
            return AIRecommendResponse(
                user_description="추천 가능한 상품이 없습니다.",
                recommended_products=[],
                ai_comment="입력 조건에 맞는 상품이 없습니다.",
            )

        # 상품 정보 준비 (GPT 프롬프트용)
        product_info = [
            {
                "id": p.id,
                "name": p.name,
                "category": str(p.category),
                "color": str(p.color),
                "price": p.price,
                "tags": [t.tag_rel.name for t in p.product_tags],
            }
            for p in candidates[:80]
        ]

        # 프롬프트 — 점수 계산식 + 가격 허용 범위 포함
        prompt = f"""
        너는 고급 인테리어 추천 AI 전문가야.
        아래의 사용자 프로필과 상품 리스트를 기반으로 사용자가 가장 선호할 상품 50개를 선정해.
        각 상품은 점수 계산식을 기반으로 평가되어야 해.

        ---

        [사용자 온보딩 정보]
        - 연령대(AgeGroup): {user_data.age_group}
        - 성별(Gender): {user_data.gender}
        - 선호 무드(MoodType): {user_data.mood_type}
        - 선호 공간(SpaceType): {user_data.space_type}

        [사용자 입력 조건]
        - 색상(Color): {filters.color}
        - 카테고리(Category): {filters.category}
        - 태그 타입(TagType): {filters.tag_type}
        - 목표 가격(Price): {filters.price} (±20% 범위 허용)

        ---

        [상품 후보 데이터]
        {json.dumps(product_info, ensure_ascii=False, indent=2)}

        ---

        ### 평가 기준 (0~1 점수)
        각 상품은 다음 항목을 기준으로 평가된다.

        #### 1. 온보딩 일치율 (0.7)
        - MoodType이 상품의 태그(tag) 또는 이름(name)에 포함되면 +0.4
        - SpaceType이 상품의 카테고리(category)와 대응되면 +0.3
        - AgeGroup과 상품 스타일/색감이 어울리면 +0.2
        - Gender가 선호할 만한 스타일이면 +0.1

        #### 2. 입력조건 일치율 (0.2)
        - Color가 동일하면 +0.3
        - Category가 동일하면 +0.3
        - TagType이 상품의 태그 중 하나와 일치하면 +0.2
        - Price가 사용자가 입력한 가격의 ±20% 범위 이내면 +0.2  
          (예: 사용자 입력이 100000이면 80000~120000 사이일 때 가산점)

        #### 3. 다양성 점수 (0.1)
        - 비슷한 Category, Color 조합이 많을수록 감점
        - Category, Color가 고르게 분포되면 가점

        #### 총점 계산식
        총점 = (온보딩 일치율 × 0.7) + (입력조건 일치율 × 0.2) + (다양성 × 0.1)

        ---

        ### 출력 형식
        - 총점을 기준으로 내림차순 정렬
        - 상위 50개의 상품 id만 JSON으로 출력
        - reasoning, 설명, 텍스트 금지
        - JSON만 반환할 것

        예시:
        {{
            "recommended": [1, 3, 5, 9, 12, 20, 33]
        }}
        """

        # GPT 호출
        ai_output = generate_text(
            prompt,
            model="gpt-4o-mini",
            system_prompt="You are a JSON generator. Return valid JSON only.",
        )

        # 응답 파싱
        try:
            parsed = json.loads(ai_output)
            recommended_ids = parsed.get("recommended", [])
        except Exception as e:
            print("AI parsing error:", e)
            print("Raw output:", ai_output[:300])
            recommended_ids = [p.id for p in candidates[:10]]

        # 매칭 및 DTO 변환
        matched_products = [p for p in candidates if p.id in recommended_ids]
        product_dtos = [
            AIRecommendedProduct(
                id=p.id,
                name=p.name,
                category=p.category,
                color=p.color,
                price=p.price,
                tags=[t.tag_rel.name for t in p.product_tags],
            )
            for p in matched_products
        ]

        # 최종 반환
        return AIRecommendResponse(
            user_description=f"{user_data.mood_type}한 {user_data.space_type} 취향의 사용자",
            recommended_products=product_dtos,
            ai_comment="온보딩·입력조건·가격·다양성 점수를 종합해 추천했습니다.",
        )
