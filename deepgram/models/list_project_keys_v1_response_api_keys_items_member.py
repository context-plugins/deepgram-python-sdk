from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListProjectKeysV1ResponseApiKeysItemsMember(SdkBaseModel):
    member_id: Optional[str] = UNSET
    email: Optional[str] = UNSET


class ListProjectKeysV1ResponseApiKeysItemsMemberDict(TypedDict):
    member_id: NotRequired[str]
    email: NotRequired[str]
