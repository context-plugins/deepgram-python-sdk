from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListenV1ResponseResultsUtterancesItemsWordsItems(SdkBaseModel):
    word: Optional[str] = UNSET
    start: Optional[float] = UNSET
    end: Optional[float] = UNSET
    confidence: Optional[float] = UNSET
    speaker: Optional[int] = UNSET
    speaker_confidence: Optional[float] = UNSET
    punctuated_word: Optional[str] = UNSET


class ListenV1ResponseResultsUtterancesItemsWordsItemsDict(TypedDict):
    word: NotRequired[str]
    start: NotRequired[float]
    end: NotRequired[float]
    confidence: NotRequired[float]
    speaker: NotRequired[int]
    speaker_confidence: NotRequired[float]
    punctuated_word: NotRequired[str]
