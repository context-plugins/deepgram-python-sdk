from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LeaveProjectV1Response(SdkBaseModel):
    message: Optional[str] = UNSET
    """confirmation message"""


class LeaveProjectV1ResponseDict(TypedDict):
    message: NotRequired[str]
