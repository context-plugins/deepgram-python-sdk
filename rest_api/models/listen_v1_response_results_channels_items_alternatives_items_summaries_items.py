from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems(SdkBaseModel):
    summary: Optional[str] = UNSET
    start_word: Optional[float] = UNSET
    end_word: Optional[float] = UNSET


class ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItemsDict(TypedDict):
    summary: NotRequired[str]
    start_word: NotRequired[float]
    end_word: NotRequired[float]
