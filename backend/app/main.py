from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router

app = FastAPI(
    title="SpentBox API",
    version="1.0.0",
)

# CORS 설정 (프론트와 연결 위해)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 중엔 *로, 배포 시엔 Vercel 도메인 등 제한
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(api_router, prefix="/api")

# 개발용 실행
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
