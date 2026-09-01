from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ListProjectKeysV1ResponseApiKeysItemsApiKey(SdkBaseModel):
    api_key_id: Optional[str] = UNSET
    comment: Optional[str] = UNSET
    scopes: Optional[list[str]] = UNSET
    created: Optional[RFC3339DateTime] = UNSET


class ListProjectKeysV1ResponseApiKeysItemsApiKeyDict(TypedDict):
    api_key_id: NotRequired[str]
    comment: NotRequired[str]
    scopes: NotRequired[list[str]]
    created: NotRequired[RFC3339DateTime]
