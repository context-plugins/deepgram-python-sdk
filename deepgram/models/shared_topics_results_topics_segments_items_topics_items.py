from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SharedTopicsResultsTopicsSegmentsItemsTopicsItems(SdkBaseModel):
    topic: Optional[str] = UNSET
    confidence_score: Optional[float] = UNSET


class SharedTopicsResultsTopicsSegmentsItemsTopicsItemsDict(TypedDict):
    topic: NotRequired[str]
    confidence_score: NotRequired[float]
