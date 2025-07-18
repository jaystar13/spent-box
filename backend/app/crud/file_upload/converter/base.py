from abc import ABC, abstractmethod
from typing import Any, Dict, List

from fastapi import UploadFile


class UploadFileBaseConverter(ABC):

    @abstractmethod
    def is_supported_file(self, file: UploadFile) -> bool:
        """처리 가능여부"""
        pass

    async def transform(self, file: UploadFile) -> List[Dict[str, Any]]:
        """파일 데이터를 정형화된 리스트로 변환"""
        df = await self.parse_raw(file)
        normalized = self.normalize(df)
        return normalized.to_dict(orient="records")

    @abstractmethod
    async def parse_raw(self, file: UploadFile) -> Any:
        """파일에서 원시 데이터 추출 (DataFrame 등)"""
        pass

    @abstractmethod
    def normalize(self, raw_data: Any) -> Any:
        """정형화된 데이터로 변환"""
        pass
