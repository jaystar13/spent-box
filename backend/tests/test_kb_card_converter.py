from io import BytesIO
from fastapi import UploadFile
import pytest

from backend.services.converter.kb_card_converter import KbCardConverter


@pytest.mark.asyncio
async def test_kb_card_converter_transform():
    # 테스트용 html 생성
    html_content = """
    <html>
        <body>
            <table id="usage1">
                <tbody id="list_pe01">
                    <tr>
                        <td>25.05.02</td>
                        <td>KB국민카드</td>
                        <td>승인</td>
                        <td>스타벅스</td>
                        <td>일시불</td>
                        <td>35,000원</td>
                    </tr>
                </tbody>
            </table>
        </body>
    </html>
    """
    fake_file = UploadFile(
        filename="kb_card_4월내역.html", file=BytesIO(html_content.encode("utf-8"))
    )

    converter = KbCardConverter()
    result = await converter.transform(fake_file)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["date"] == "2025-05-02"
    assert result[0]["amount"] == 35000
    assert result[0]["merchant"] == "스타벅스"
    assert result[0]["cardName"] == "KB국민카드"
