from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_project_invites_v1_response_invites_items import (
    ListProjectInvitesV1ResponseInvitesItems,
    ListProjectInvitesV1ResponseInvitesItemsDict,
)


class ListProjectInvitesV1Response(SdkBaseModel):
    invites: Optional[list[ListProjectInvitesV1ResponseInvitesItems]] = UNSET


class ListProjectInvitesV1ResponseDict(TypedDict):
    invites: NotRequired[list[ListProjectInvitesV1ResponseInvitesItemsDict]]
