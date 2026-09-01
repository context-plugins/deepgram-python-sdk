from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems(SdkBaseModel):
    label: Optional[str] = UNSET
    value: Optional[str] = UNSET
    raw_value: Optional[str] = UNSET
    confidence: Optional[float] = UNSET
    start_word: Optional[float] = UNSET
    end_word: Optional[float] = UNSET


class ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItemsDict(TypedDict):
    label: NotRequired[str]
    value: NotRequired[str]
    raw_value: NotRequired[str]
    confidence: NotRequired[float]
    start_word: NotRequired[float]
    end_word: NotRequired[float]
