from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems(SdkBaseModel):
    word: Optional[str] = UNSET
    start: Optional[float] = UNSET
    end: Optional[float] = UNSET
    confidence: Optional[float] = UNSET


class ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItemsDict(TypedDict):
    word: NotRequired[str]
    start: NotRequired[float]
    end: NotRequired[float]
    confidence: NotRequired[float]
