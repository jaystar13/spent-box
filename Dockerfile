FROM python:3.11-slim

# 1. 필요한 시스템 패키지 설치
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 2. poetry 설치 (공식 설치 스크립트 사용)
RUN curl -sSL https://install.python-poetry.org | python3 -

# 3. 환경 변수 설정
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH=/app/backend

# 4. 작업 디렉토리 설정
WORKDIR /app

# 5. poetry 관련 파일 복사
COPY backend/pyproject.toml backend/poetry.lock* /app/backend/
COPY .env /app/.env

# 6. 종속성 설치
WORKDIR /app/backend
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# 7. 소스 복사
COPY backend/ /app/backend/
#COPY backend/README.md /app/backend/README.md

# 8. 서버 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]