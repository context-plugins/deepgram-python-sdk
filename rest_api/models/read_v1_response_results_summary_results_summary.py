from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReadV1ResponseResultsSummaryResultsSummary(SdkBaseModel):
    text: Optional[str] = UNSET


class ReadV1ResponseResultsSummaryResultsSummaryDict(TypedDict):
    text: NotRequired[str]
