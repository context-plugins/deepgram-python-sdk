from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsageV1ResponseResolution(SdkBaseModel):
    units: Optional[str] = UNSET
    amount: Optional[float] = UNSET


class UsageV1ResponseResolutionDict(TypedDict):
    units: NotRequired[str]
    amount: NotRequired[float]
