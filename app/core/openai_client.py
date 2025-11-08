from openai import OpenAI
from app.core.config import OPENAI_API_KEY
import re
import json

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_text(
    prompt: str,
    model: str = "gpt-4o",
    max_tokens: int = 2000,
    system_prompt: str = "You are a JSON generator. Always return valid JSON only, with no explanation or commentary.",
) -> str:
    """
    OpenAI API 호출 함수 (JSON 응답 전용)
    """
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
    )

    content = response.choices[0].message.content.strip()

    # ✅ 백틱(```json`, ``` 등) 제거
    content = re.sub(r"^```(json)?", "", content.strip())
    content = re.sub(r"```$", "", content.strip())
    content = content.strip()

    # ✅ JSON 유효성 검사
    try:
        json.loads(content)
        return content
    except json.JSONDecodeError:
        print("⚠️ GPT returned invalid JSON, raw output:")
        print(content[:300])
        return '{"recommended": []}'
