from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from backend.deps.auth import get_current_user_id
from backend.services.file_analyzer_service import analyze_uploaded_file

router = APIRouter()


@router.post("/analyze")
async def analyze_uploaded_file_api(
    file: UploadFile = File(...),
    institution: str = Form(...),
    user_id: int = Depends(get_current_user_id),
):
    try:
        result = await analyze_uploaded_file(
            file=file, institution=institution, user_id=user_id
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
