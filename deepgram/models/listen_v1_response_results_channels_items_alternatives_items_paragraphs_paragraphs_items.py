from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .listen_v1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items_sentences_items import (
    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems,
    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItemsDict,
)


class ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems(SdkBaseModel):
    sentences: Optional[
        list[ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems]
    ] = UNSET
    speaker: Optional[int] = UNSET
    num_words: Optional[int] = UNSET
    start: Optional[float] = UNSET
    end: Optional[float] = UNSET


class ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsDict(TypedDict):
    sentences: NotRequired[
        list[ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItemsDict]
    ]
    speaker: NotRequired[int]
    num_words: NotRequired[int]
    start: NotRequired[float]
    end: NotRequired[float]
