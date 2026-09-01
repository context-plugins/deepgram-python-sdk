from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shared_topics_results_topics_segments_items_topics_items import (
    SharedTopicsResultsTopicsSegmentsItemsTopicsItems,
    SharedTopicsResultsTopicsSegmentsItemsTopicsItemsDict,
)


class SharedTopicsResultsTopicsSegmentsItems(SdkBaseModel):
    text: Optional[str] = UNSET
    start_word: Optional[float] = UNSET
    end_word: Optional[float] = UNSET
    topics: Optional[list[SharedTopicsResultsTopicsSegmentsItemsTopicsItems]] = UNSET


class SharedTopicsResultsTopicsSegmentsItemsDict(TypedDict):
    text: NotRequired[str]
    start_word: NotRequired[float]
    end_word: NotRequired[float]
    topics: NotRequired[
        list[SharedTopicsResultsTopicsSegmentsItemsTopicsItems | SharedTopicsResultsTopicsSegmentsItemsTopicsItemsDict]
    ]
