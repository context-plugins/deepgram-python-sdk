from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListenV1ResponseResultsSummary(SdkBaseModel):
    result: Optional[str] = UNSET
    short: Optional[str] = UNSET


class ListenV1ResponseResultsSummaryDict(TypedDict):
    result: NotRequired[str]
    short: NotRequired[str]
