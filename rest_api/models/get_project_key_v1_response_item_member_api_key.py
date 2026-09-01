from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class GetProjectKeyV1ResponseItemMemberApiKey(SdkBaseModel):
    api_key_id: Optional[str] = UNSET
    comment: Optional[str] = UNSET
    scopes: Optional[list[str]] = UNSET
    tags: Optional[list[str]] = UNSET
    expiration_date: Optional[RFC3339DateTime] = UNSET
    created: Optional[RFC3339DateTime] = UNSET


class GetProjectKeyV1ResponseItemMemberApiKeyDict(TypedDict):
    api_key_id: NotRequired[str]
    comment: NotRequired[str]
    scopes: NotRequired[list[str]]
    tags: NotRequired[list[str]]
    expiration_date: NotRequired[RFC3339DateTime]
    created: NotRequired[RFC3339DateTime]
