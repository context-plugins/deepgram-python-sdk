from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdateProjectMemberScopesV1Response(SdkBaseModel):
    message: Optional[str] = UNSET
    """confirmation message"""


class UpdateProjectMemberScopesV1ResponseDict(TypedDict):
    message: NotRequired[str]
