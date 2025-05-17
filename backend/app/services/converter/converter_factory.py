from app.services.converter.base_converter import BaseConverter
from app.services.converter.hana_card_converter import HanaCardConverter
from app.services.converter.hyundai_card_converter import HyundaiCardConverter
from app.services.converter.kb_card_converter import KbCardConverter


def get_converter(institution: str) -> BaseConverter:
    mapping = {
        "kb-card": KbCardConverter,
        "hyundai-card": HyundaiCardConverter,
        "hana-card": HanaCardConverter,
    }

    cls = mapping.get(institution.lower())
    if not cls:
        raise ValueError(f"{institution} 기관은 현재 지원되지 않습니다.")
    return cls()
