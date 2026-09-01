from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems(SdkBaseModel):
    confidence: Optional[float] = UNSET
    start: Optional[float] = UNSET
    end: Optional[float] = UNSET
    snippet: Optional[str] = UNSET


class ListenV1ResponseResultsChannelsItemsSearchItemsHitsItemsDict(TypedDict):
    confidence: NotRequired[float]
    start: NotRequired[float]
    end: NotRequired[float]
    snippet: NotRequired[str]
