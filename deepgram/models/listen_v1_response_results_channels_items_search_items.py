from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .listen_v1_response_results_channels_items_search_items_hits_items import (
    ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems,
    ListenV1ResponseResultsChannelsItemsSearchItemsHitsItemsDict,
)


class ListenV1ResponseResultsChannelsItemsSearchItems(SdkBaseModel):
    query: Optional[str] = UNSET
    hits: Optional[list[ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems]] = UNSET


class ListenV1ResponseResultsChannelsItemsSearchItemsDict(TypedDict):
    query: NotRequired[str]
    hits: NotRequired[list[ListenV1ResponseResultsChannelsItemsSearchItemsHitsItemsDict]]
