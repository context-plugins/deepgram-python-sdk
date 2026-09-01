from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_project_keys_v1_response_api_keys_items import (
    ListProjectKeysV1ResponseApiKeysItems,
    ListProjectKeysV1ResponseApiKeysItemsDict,
)


class ListProjectKeysV1Response(SdkBaseModel):
    api_keys: Optional[list[ListProjectKeysV1ResponseApiKeysItems]] = UNSET


class ListProjectKeysV1ResponseDict(TypedDict):
    api_keys: NotRequired[list[ListProjectKeysV1ResponseApiKeysItems | ListProjectKeysV1ResponseApiKeysItemsDict]]
