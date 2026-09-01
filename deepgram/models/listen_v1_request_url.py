from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ListenV1RequestUrl(SdkBaseModel):
    """Audio file URL to transcribe"""

    url: str


class ListenV1RequestUrlDict(TypedDict):
    url: str
