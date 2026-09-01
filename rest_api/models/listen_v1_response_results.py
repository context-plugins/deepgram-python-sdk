from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .listen_v1_response_results_channels_items import (
    ListenV1ResponseResultsChannelsItems,
    ListenV1ResponseResultsChannelsItemsDict,
)
from .listen_v1_response_results_summary import ListenV1ResponseResultsSummary, ListenV1ResponseResultsSummaryDict
from .listen_v1_response_results_utterances_items import (
    ListenV1ResponseResultsUtterancesItems,
    ListenV1ResponseResultsUtterancesItemsDict,
)
from .shared_intents import SharedIntents, SharedIntentsDict
from .shared_sentiments import SharedSentiments, SharedSentimentsDict
from .shared_topics import SharedTopics, SharedTopicsDict


class ListenV1ResponseResults(SdkBaseModel):
    channels: list[ListenV1ResponseResultsChannelsItems]
    utterances: Optional[list[ListenV1ResponseResultsUtterancesItems]] = UNSET
    summary: Optional[ListenV1ResponseResultsSummary] = UNSET
    topics: Optional[SharedTopics] = UNSET
    """Output whenever ``topics=true`` is used"""

    intents: Optional[SharedIntents] = UNSET
    """Output whenever ``intents=true`` is used"""

    sentiments: Optional[SharedSentiments] = UNSET
    """Output whenever ``sentiment=true`` is used"""


class ListenV1ResponseResultsDict(TypedDict):
    channels: list[ListenV1ResponseResultsChannelsItems | ListenV1ResponseResultsChannelsItemsDict]
    utterances: NotRequired[list[ListenV1ResponseResultsUtterancesItems | ListenV1ResponseResultsUtterancesItemsDict]]
    summary: NotRequired[ListenV1ResponseResultsSummary | ListenV1ResponseResultsSummaryDict]
    topics: NotRequired[SharedTopics | SharedTopicsDict]
    intents: NotRequired[SharedIntents | SharedIntentsDict]
    sentiments: NotRequired[SharedSentiments | SharedSentimentsDict]
