from __future__ import annotations

from typing import TypeAlias

from ..read_v1_request_text import ReadV1RequestText, ReadV1RequestTextDict
from ..read_v1_request_url import ReadV1RequestUrl, ReadV1RequestUrlDict

ReadV1Request: TypeAlias = ReadV1RequestUrl | ReadV1RequestText

ReadV1RequestDict: TypeAlias = ReadV1RequestUrlDict | ReadV1RequestTextDict
