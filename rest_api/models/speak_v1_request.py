from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SpeakV1Request(SdkBaseModel):
    """Request body for text-to-speech conversion"""

    text: str
    """The text content to be converted to speech"""


class SpeakV1RequestDict(TypedDict):
    text: str
