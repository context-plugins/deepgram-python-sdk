from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_project_key_v1_response_item_member_api_key import (
    GetProjectKeyV1ResponseItemMemberApiKey,
    GetProjectKeyV1ResponseItemMemberApiKeyDict,
)


class GetProjectKeyV1ResponseItemMember(SdkBaseModel):
    member_id: Optional[str] = UNSET
    email: Optional[str] = UNSET
    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    api_key: Optional[GetProjectKeyV1ResponseItemMemberApiKey] = UNSET


class GetProjectKeyV1ResponseItemMemberDict(TypedDict):
    member_id: NotRequired[str]
    email: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    api_key: NotRequired[GetProjectKeyV1ResponseItemMemberApiKey | GetProjectKeyV1ResponseItemMemberApiKeyDict]
