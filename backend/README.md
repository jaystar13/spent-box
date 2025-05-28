# 프로젝트 실행 가이드

이 프로젝트는 Docker와 PostgreSQL을 기반으로 개발 및 테스트 환경을 구성합니다. 데이터베이스 마이그레이션은 Alembic을 사용하며, 테스트는 pytest로 수행됩니다.

---

## ✅ 실행 순서

### 1. 도커 컨테이너 실행

```
docker-compose up -d
```

> PostgreSQL 등 종속 서비스가 컨테이너로 실행됩니다.

---

### 2. Alembic Revision 파일 생성

```
alembic revision --autogenerate -m "create tables"
```

> 모델이 정의된 후에 실행해야 하며, 자동으로 생성된 마이그레이션 파일은 반드시 검토 후 적용하세요.

---

### 3. Revision 파일 확인 및 수정

`alembic/versions/` 디렉토리 아래 생성된 파일을 열어 변경 사항을 확인하고, 필요시 수정합니다.

---

### 4. 마이그레이션 적용 (테이블 생성)

```
alembic upgrade head
```

> 최신 revision까지 데이터베이스에 적용됩니다.

---

### 5. 테스트 실행

```
PYTHONPATH=. pytest app/tests/api/routes/test_users.py
```

> 루트 디렉토리를 import 경로에 포함시켜 테스트 모듈들이 정상적으로 로딩되도록 합니다.

---

## 📁 디렉토리 구조 예시

```
project-root/
├── app/
│   ├── models/
│   ├── tests/
│   └── ...
├── alembic/
│   ├── versions/
│   └── env.py
├── docker-compose.yml
├── alembic.ini
├── README.md
└── ...
```

---

## 🔧 필요 패키지 (예시)

- SQLAlchemy
- Alembic
- psycopg2-binary
- pytest

> 패키지 설치는 `requirements.txt` 또는 `pyproject.toml`을 이용하세요.

---

## 💬 참고

- Alembic 설정: `alembic/env.py`에서 `target_metadata` 설정이 올바르게 되어 있어야 `--autogenerate`가 정상 작동합니다.
- PostgreSQL은 docker-compose 내에서 `db`라는 서비스명으로 접근 가능합니다 (`host: db`, `port: 5432` 등).
