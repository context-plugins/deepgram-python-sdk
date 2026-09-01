from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeleteProjectInviteV1Response(SdkBaseModel):
    message: Optional[str] = UNSET
    """confirmation message"""


class DeleteProjectInviteV1ResponseDict(TypedDict):
    message: NotRequired[str]
