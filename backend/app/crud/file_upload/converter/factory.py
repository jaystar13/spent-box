from app.crud.file_upload.converter.base import UploadFileBaseConverter
from app.crud.file_upload.converter.kb_card_converter import KbCardConverter


def get_converter(institution: str) -> UploadFileBaseConverter:
    mapping = {"kb-card": KbCardConverter}

    cls = mapping.get(institution.lower())
    if not cls:
        raise ValueError(f"{institution} 기관은 현재 지원되지 않습니다.")
    return cls()
