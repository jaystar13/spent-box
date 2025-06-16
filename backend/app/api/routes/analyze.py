from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.crud.analyzer import analyze_file, validate_file
from app.api.deps import CurrentUser


router = APIRouter(prefix="/analyze-upload", tags=["analyze"])


@router.post("/")
def analyze_upload(
    current_user: CurrentUser,
    year: int = Form(...),
    month: int = Form(...),
    payment_method: str = Form(...),
    file: UploadFile = File(...),
):
    # 1. 유효성 체크
    if not validate_file(file):
        raise HTTPException(
            status_code=400, detail="엑셀(.xlsx, .xls) 파일만 업로드 가능합니다."
        )

    # 2. 분석 처리
    result = analyze_file(
        current_user=current_user,
        year=year,
        month=month,
        payment_method=payment_method,
        file=file,
    )

    return {"status": "success", "institution": payment_method, "summary": result}
