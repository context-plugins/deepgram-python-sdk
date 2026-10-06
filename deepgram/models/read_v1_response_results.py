from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .read_v1_response_results_summary import ReadV1ResponseResultsSummary, ReadV1ResponseResultsSummaryDict
from .shared_intents import SharedIntents, SharedIntentsDict
from .shared_sentiments import SharedSentiments, SharedSentimentsDict
from .shared_topics import SharedTopics, SharedTopicsDict


class ReadV1ResponseResults(SdkBaseModel):
    summary: Optional[ReadV1ResponseResultsSummary] = UNSET
    """Output whenever ``summary=true`` is used"""

    topics: Optional[SharedTopics] = UNSET
    """Output whenever ``topics=true`` is used"""

    intents: Optional[SharedIntents] = UNSET
    """Output whenever ``intents=true`` is used"""

    sentiments: Optional[SharedSentiments] = UNSET
    """Output whenever ``sentiment=true`` is used"""


class ReadV1ResponseResultsDict(TypedDict):
    summary: NotRequired[ReadV1ResponseResultsSummaryDict]
    topics: NotRequired[SharedTopicsDict]
    intents: NotRequired[SharedIntentsDict]
    sentiments: NotRequired[SharedSentimentsDict]
