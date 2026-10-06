from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_project_keys_v1_response_api_keys_items_api_key import (
    ListProjectKeysV1ResponseApiKeysItemsApiKey,
    ListProjectKeysV1ResponseApiKeysItemsApiKeyDict,
)
from .list_project_keys_v1_response_api_keys_items_member import (
    ListProjectKeysV1ResponseApiKeysItemsMember,
    ListProjectKeysV1ResponseApiKeysItemsMemberDict,
)


class ListProjectKeysV1ResponseApiKeysItems(SdkBaseModel):
    member: Optional[ListProjectKeysV1ResponseApiKeysItemsMember] = UNSET
    api_key: Optional[ListProjectKeysV1ResponseApiKeysItemsApiKey] = UNSET


class ListProjectKeysV1ResponseApiKeysItemsDict(TypedDict):
    member: NotRequired[ListProjectKeysV1ResponseApiKeysItemsMemberDict]
    api_key: NotRequired[ListProjectKeysV1ResponseApiKeysItemsApiKeyDict]
