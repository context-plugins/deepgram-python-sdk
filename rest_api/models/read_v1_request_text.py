from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ReadV1RequestText(SdkBaseModel):
    text: str
    """The plain text to analyze"""


class ReadV1RequestTextDict(TypedDict):
    text: str
