from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ReadV1RequestUrl(SdkBaseModel):
    url: str
    """A URL pointing to the text source"""


class ReadV1RequestUrlDict(TypedDict):
    url: str
