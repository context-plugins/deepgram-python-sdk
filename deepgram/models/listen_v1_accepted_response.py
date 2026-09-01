from __future__ import annotations

from uuid import UUID

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ListenV1AcceptedResponse(SdkBaseModel):
    """Accepted response for asynchronous transcription requests"""

    request_id: UUID
    """Unique identifier for tracking the asynchronous request"""


class ListenV1AcceptedResponseDict(TypedDict):
    request_id: UUID
