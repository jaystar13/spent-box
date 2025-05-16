from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
