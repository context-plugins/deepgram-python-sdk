from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListProjectInvitesV1ResponseInvitesItems(SdkBaseModel):
    email: Optional[str] = UNSET
    """The email address of the invitee"""

    scope: Optional[str] = UNSET
    """The scope of the invitee"""


class ListProjectInvitesV1ResponseInvitesItemsDict(TypedDict):
    email: NotRequired[str]
    scope: NotRequired[str]
