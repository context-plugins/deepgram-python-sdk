from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .listen_v1_response_results_channels_items_alternatives_items_entities_items import (
    ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems,
    ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItemsDict,
)
from .listen_v1_response_results_channels_items_alternatives_items_paragraphs import (
    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs,
    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsDict,
)
from .listen_v1_response_results_channels_items_alternatives_items_summaries_items import (
    ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems,
    ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItemsDict,
)
from .listen_v1_response_results_channels_items_alternatives_items_topics_items import (
    ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems,
    ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItemsDict,
)
from .listen_v1_response_results_channels_items_alternatives_items_words_items import (
    ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems,
    ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItemsDict,
)


class ListenV1ResponseResultsChannelsItemsAlternativesItems(SdkBaseModel):
    transcript: Optional[str] = UNSET
    confidence: Optional[float] = UNSET
    words: Optional[list[ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems]] = UNSET
    paragraphs: Optional[ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs] = UNSET
    entities: Optional[list[ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems]] = UNSET
    summaries: Optional[list[ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems]] = UNSET
    topics: Optional[list[ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems]] = UNSET


class ListenV1ResponseResultsChannelsItemsAlternativesItemsDict(TypedDict):
    transcript: NotRequired[str]
    confidence: NotRequired[float]
    words: NotRequired[
        list[
            (
                ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems
                | ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItemsDict
            )
        ]
    ]
    paragraphs: NotRequired[
        (
            ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs
            | ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsDict
        )
    ]
    entities: NotRequired[
        list[
            (
                ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems
                | ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItemsDict
            )
        ]
    ]
    summaries: NotRequired[
        list[
            (
                ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems
                | ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItemsDict
            )
        ]
    ]
    topics: NotRequired[
        list[
            (
                ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems
                | ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItemsDict
            )
        ]
    ]
