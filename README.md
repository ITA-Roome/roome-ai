# Roome_AI

잇타(It's TIME) 8기 2팀 Roome AI Repository
FastAPI + MySQL + AI 기반 서버입니다.

FastAPI와 AWS RDS(MySQL)를 이용해 서버를 로컬 환경에서 실행할 수 있습니다.<br>
아래 단계를 순서대로 따라 하면 바로 구동됩니다.

---

## 로컬 실행 방법

**저장소 클론**

```bash
git clone https://github.com/its-time-team8/roome-ai.git
cd roome-ai
```

**환경 변수 파일 생성**  
루트 디렉토리에 `.env` 파일을 생성하고 환경 변수를 추가합니다.

**의존성 설치**

```bash
make install
```

**서버 실행**

```bash
make run-dev
```

**서버 확인**

```bash
서버가 정상적으로 실행되면 아래 주소에서 확인할 수 있습니다.
Root → [http://localhost:8000/](http://localhost:8000/)
=>{"message":"Welcome to Roome AI!"}
```

**서버 종료**

```bash
# 터미널에서 Ctrl + C
```

---

## 주요 명령어 요약

| 명령어         | 설명                         |
| -------------- | ---------------------------- |
| `make install` | 가상환경 생성 및 의존성 설치 |
| `make run-dev` | FastAPI 개발 서버 실행       |
| `make clean`   | 캐시 및 임시 파일 삭제       |
| `make reset`   | 가상환경 초기화              |

---

## Requirements

-   Python 3.10+
-   Make (macOS 기본 탑재, Windows는 Git Bash 권장)
-   MySQL 8.x (AWS RDS 또는 로컬)
-   Virtualenv (자동 생성됨)

### Python Dependencies

-   **FastAPI** 0.115.0
-   **Uvicorn** 0.30.6
-   **SQLAlchemy** 2.0.36
-   **mysqlclient** 2.2.5
-   **PyMySQL** 1.1.1
-   **python-dotenv** 1.0.1
-   **python-jose** 3.3.0
-   **passlib[bcrypt]** 1.7.4
-   **email-validator** 2.2.0
-   **loguru** 0.7.2
-   **pytest** 8.3.2
-   **pytest-asyncio** 0.24.0

---

## License

본 프로젝트는 잇타(It's TIME) 8기 2팀 **Roome AI** 내부 개발용입니다.
