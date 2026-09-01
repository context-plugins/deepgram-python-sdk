from __future__ import annotations

from uuid import UUID

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SpeakV2AcceptedResponse(SdkBaseModel):
    """Accepted response returned when a callback URL is supplied; the audio is delivered asynchronously to that URL."""

    request_id: UUID
    """Unique identifier for tracking the asynchronous request"""


class SpeakV2AcceptedResponseDict(TypedDict):
    request_id: UUID
