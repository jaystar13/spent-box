from backend.services.converter.base_converter import BaseConverter
from backend.services.converter.kb_card_converter import KbCardConverter


def get_converter(institution: str) -> BaseConverter:
    mapping = {
        "kb-card": KbCardConverter,
    }

    cls = mapping.get(institution.lower())
    if not cls:
        raise ValueError(f"{institution} 기관은 현재 지원되지 않습니다.")
    return cls()
