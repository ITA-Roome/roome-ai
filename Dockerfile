# ---- Builder ----
FROM python:3.10-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y build-essential libpq-dev default-libmysqlclient-dev pkg-config && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

# ---- Runtime ----
FROM python:3.10-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY . .

CMD ["uvicorn", "app.main:app","--host", "0.0.0.0","--port","8000"]
