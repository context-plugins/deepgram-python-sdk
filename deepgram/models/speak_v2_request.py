from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SpeakV2Request(SdkBaseModel):
    """Request body for Flux TTS batch (REST) text-to-speech conversion. The full block of text is synthesized in a
    single request and returned as one audio response."""

    text: str
    """The text content to be converted to speech. The server normalizes and preprocesses the text (e.g. stripping
    inline controls) before synthesis."""


class SpeakV2RequestDict(TypedDict):
    text: str
