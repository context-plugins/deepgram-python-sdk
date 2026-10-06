from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .listen_v1_response_results_utterances_items_words_items import (
    ListenV1ResponseResultsUtterancesItemsWordsItems,
    ListenV1ResponseResultsUtterancesItemsWordsItemsDict,
)


class ListenV1ResponseResultsUtterancesItems(SdkBaseModel):
    start: Optional[float] = UNSET
    end: Optional[float] = UNSET
    confidence: Optional[float] = UNSET
    channel: Optional[int] = UNSET
    transcript: Optional[str] = UNSET
    words: Optional[list[ListenV1ResponseResultsUtterancesItemsWordsItems]] = UNSET
    speaker: Optional[int] = UNSET
    id: Optional[UUID] = UNSET


class ListenV1ResponseResultsUtterancesItemsDict(TypedDict):
    start: NotRequired[float]
    end: NotRequired[float]
    confidence: NotRequired[float]
    channel: NotRequired[int]
    transcript: NotRequired[str]
    words: NotRequired[list[ListenV1ResponseResultsUtterancesItemsWordsItemsDict]]
    speaker: NotRequired[int]
    id: NotRequired[UUID]
