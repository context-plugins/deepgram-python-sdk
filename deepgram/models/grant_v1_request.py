from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GrantV1Request(SdkBaseModel):
    ttl_seconds: Optional[float] = UNSET
    """Time to live in seconds for the token. Defaults to 30 seconds."""


class GrantV1RequestDict(TypedDict):
    ttl_seconds: NotRequired[float]
