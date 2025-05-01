from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from backend.deps.auth import get_current_user_id

router = APIRouter()


@router.post("/upload/analyze")
async def analyze_uploaded_file_api(
    file: UploadFile = File(...), user_id: int = Depends(get_current_user_id)
):
    try:
        result = await analyze_uploaded_file(user_id, file)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
