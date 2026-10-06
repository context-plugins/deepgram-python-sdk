from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_project_key_v1_response_item_member import (
    GetProjectKeyV1ResponseItemMember,
    GetProjectKeyV1ResponseItemMemberDict,
)


class GetProjectKeyV1ResponseItem(SdkBaseModel):
    member: Optional[GetProjectKeyV1ResponseItemMember] = UNSET


class GetProjectKeyV1ResponseItemDict(TypedDict):
    member: NotRequired[GetProjectKeyV1ResponseItemMemberDict]
