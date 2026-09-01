from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class CreateKeyV1Response(SdkBaseModel):
    """API key created"""

    api_key_id: Optional[str] = UNSET
    """The unique identifier of the API key"""

    key: Optional[str] = UNSET
    """The API key"""

    comment: Optional[str] = UNSET
    """A comment for the API key"""

    scopes: Optional[list[str]] = UNSET
    """The scopes for the API key"""

    tags: Optional[list[str]] = UNSET
    """The tags for the API key"""

    expiration_date: Optional[RFC3339DateTime] = UNSET
    """The expiration date of the API key"""


class CreateKeyV1ResponseDict(TypedDict):
    api_key_id: NotRequired[str]
    key: NotRequired[str]
    comment: NotRequired[str]
    scopes: NotRequired[list[str]]
    tags: NotRequired[list[str]]
    expiration_date: NotRequired[RFC3339DateTime]
