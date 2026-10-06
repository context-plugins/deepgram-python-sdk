from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .listen_v1_response_results_channels_items_alternatives_items import (
    ListenV1ResponseResultsChannelsItemsAlternativesItems,
    ListenV1ResponseResultsChannelsItemsAlternativesItemsDict,
)
from .listen_v1_response_results_channels_items_search_items import (
    ListenV1ResponseResultsChannelsItemsSearchItems,
    ListenV1ResponseResultsChannelsItemsSearchItemsDict,
)


class ListenV1ResponseResultsChannelsItems(SdkBaseModel):
    search: Optional[list[ListenV1ResponseResultsChannelsItemsSearchItems]] = UNSET
    alternatives: Optional[list[ListenV1ResponseResultsChannelsItemsAlternativesItems]] = UNSET
    detected_language: Optional[str] = UNSET


class ListenV1ResponseResultsChannelsItemsDict(TypedDict):
    search: NotRequired[list[ListenV1ResponseResultsChannelsItemsSearchItemsDict]]
    alternatives: NotRequired[list[ListenV1ResponseResultsChannelsItemsAlternativesItemsDict]]
    detected_language: NotRequired[str]
