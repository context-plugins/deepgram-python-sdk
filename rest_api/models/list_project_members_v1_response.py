from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_project_members_v1_response_members_items import (
    ListProjectMembersV1ResponseMembersItems,
    ListProjectMembersV1ResponseMembersItemsDict,
)


class ListProjectMembersV1Response(SdkBaseModel):
    members: Optional[list[ListProjectMembersV1ResponseMembersItems]] = UNSET


class ListProjectMembersV1ResponseDict(TypedDict):
    members: NotRequired[list[ListProjectMembersV1ResponseMembersItems | ListProjectMembersV1ResponseMembersItemsDict]]
