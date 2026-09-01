from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems(SdkBaseModel):
    text: Optional[str] = UNSET
    start_word: Optional[float] = UNSET
    end_word: Optional[float] = UNSET
    topics: Optional[list[str]] = UNSET


class ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItemsDict(TypedDict):
    text: NotRequired[str]
    start_word: NotRequired[float]
    end_word: NotRequired[float]
    topics: NotRequired[list[str]]
