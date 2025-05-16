from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from backend.deps.auth import get_current_user_id
from backend.schemas.file_analyzer_schemas import FileAnalyzeRequest
from backend.services.file_analyzer_service import analyze_uploaded_file

router = APIRouter()


# 요청 객체 생성용 의존성 함수
def get_file_analyze_request(
    institution: str = Form(...),
    year: int = Form(...),
    month: int = Form(...),
    user_id: int = Depends(get_current_user_id),
):
    return FileAnalyzeRequest(
        institution=institution, year=year, month=month, user_id=user_id
    )


@router.post("/analyze")
async def analyze_uploaded_file_api(
    file: UploadFile = File(...),
    request: FileAnalyzeRequest = Depends(get_file_analyze_request),
):
    try:
        result = await analyze_uploaded_file(file=file, request=request)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
