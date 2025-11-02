# ===========================================
# Roome FastAPI Makefile (dotenv + MySQL)
# ===========================================
APP_NAME = roome_ai
PYTHON = python3
VENV = venv
UVICORN = $(VENV)/bin/uvicorn
HOST = localhost
PORT = 8000

# -------------------------------------------
# 환경 구성
# -------------------------------------------
install:
	@echo "Setting up virtual environment and installing dependencies..."
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt
	@echo "Dependencies installed successfully!"

# -------------------------------------------
# 서버 실행(우선 로컬 환경만)
# -------------------------------------------
run-dev:
	@echo "Starting FastAPI server..."
	PYTHONPATH=. $(UVICORN) app.main:app --host $(HOST) --port $(PORT) --reload

# -------------------------------------------
# 테스트 실행
# -------------------------------------------
test:
	@echo "Running tests..."
	PYTHONPATH=. $(VENV)/bin/pytest -v --disable-warnings

# -------------------------------------------
# 코드 정리
# -------------------------------------------
format:
	@echo "Formatting code..."
	$(VENV)/bin/black app tests || true

lint:
	@echo "Linting code..."
	$(VENV)/bin/flake8 app tests || true

# -------------------------------------------
# 정리 및 초기화
# -------------------------------------------
clean:
	@echo "Cleaning cache and temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

reset: clean
	@echo "Resetting environment..."
	rm -rf $(VENV)
	@echo "Environment reset complete."
