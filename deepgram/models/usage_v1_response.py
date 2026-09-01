from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .usage_v1_response_resolution import UsageV1ResponseResolution, UsageV1ResponseResolutionDict


class UsageV1Response(SdkBaseModel):
    start: Optional[Date] = UNSET
    end: Optional[Date] = UNSET
    resolution: Optional[UsageV1ResponseResolution] = UNSET


class UsageV1ResponseDict(TypedDict):
    start: NotRequired[Date]
    end: NotRequired[Date]
    resolution: NotRequired[UsageV1ResponseResolution | UsageV1ResponseResolutionDict]
