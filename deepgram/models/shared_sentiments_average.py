from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SharedSentimentsAverage(SdkBaseModel):
    sentiment: Optional[str] = UNSET
    sentiment_score: Optional[float] = UNSET


class SharedSentimentsAverageDict(TypedDict):
    sentiment: NotRequired[str]
    sentiment_score: NotRequired[float]
