from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .listen_v1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items import (
    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems,
    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsDict,
)


class ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs(SdkBaseModel):
    transcript: Optional[str] = UNSET
    paragraphs: Optional[list[ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems]] = UNSET


class ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsDict(TypedDict):
    transcript: NotRequired[str]
    paragraphs: NotRequired[list[ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsDict]]
