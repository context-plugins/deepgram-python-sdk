from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListProjectMemberScopesV1Response(SdkBaseModel):
    scopes: Optional[list[str]] = UNSET
    """The API scopes of the member"""


class ListProjectMemberScopesV1ResponseDict(TypedDict):
    scopes: NotRequired[list[str]]
