from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeleteProjectV1Response(SdkBaseModel):
    message: Optional[str] = UNSET
    """Confirmation message"""


class DeleteProjectV1ResponseDict(TypedDict):
    message: NotRequired[str]
