from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SharedIntentsResultsIntentsSegmentsItemsIntentsItems(SdkBaseModel):
    intent: Optional[str] = UNSET
    confidence_score: Optional[float] = UNSET


class SharedIntentsResultsIntentsSegmentsItemsIntentsItemsDict(TypedDict):
    intent: NotRequired[str]
    confidence_score: NotRequired[float]
