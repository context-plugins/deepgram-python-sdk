from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListProjectMembersV1ResponseMembersItems(SdkBaseModel):
    member_id: Optional[str] = UNSET
    """The unique identifier of the member"""

    scopes: Optional[list[str]] = UNSET
    """The API scopes of the member"""

    email: Optional[str] = UNSET
    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET


class ListProjectMembersV1ResponseMembersItemsDict(TypedDict):
    member_id: NotRequired[str]
    scopes: NotRequired[list[str]]
    email: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
