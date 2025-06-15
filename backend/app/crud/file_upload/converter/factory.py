from app.crud.file_upload.converter.base import UploadFileBaseConverter
from app.crud.file_upload.converter.kb_card_converter import KbCardConverter


def get_converter(payment_method: str) -> UploadFileBaseConverter:
    mapping = {"kb-card": KbCardConverter}

    cls = mapping.get(payment_method.lower())
    if not cls:
        raise ValueError(f"{payment_method} 결제방법은 현재 지원되지 않습니다.")
    return cls()
