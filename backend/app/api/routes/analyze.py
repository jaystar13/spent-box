from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.crud.analyzer import analyze_file, validate_file


router = APIRouter(prefix="/analyze-upload", tags=["analyze"])


@router.post
async def analyze_upload(institution: str = Form(...), file: UploadFile = File(...)):
    # 1. 유효성 체크
    if not validate_file(file):
        raise HTTPException(
            status_code=400, detail="엑셀(.xlsx, .xls) 파일만 업로드 가능합니다."
        )

    # 2. 분석 처리
    result = await analyze_file(file, institution)

    return {"status": "success", "institution": institution, "summary": result}
