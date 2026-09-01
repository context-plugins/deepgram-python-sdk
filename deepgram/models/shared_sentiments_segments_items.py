from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SharedSentimentsSegmentsItems(SdkBaseModel):
    text: Optional[str] = UNSET
    start_word: Optional[float] = UNSET
    end_word: Optional[float] = UNSET
    sentiment: Optional[str] = UNSET
    sentiment_score: Optional[float] = UNSET


class SharedSentimentsSegmentsItemsDict(TypedDict):
    text: NotRequired[str]
    start_word: NotRequired[float]
    end_word: NotRequired[float]
    sentiment: NotRequired[str]
    sentiment_score: NotRequired[float]
