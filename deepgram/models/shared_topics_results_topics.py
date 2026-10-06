from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shared_topics_results_topics_segments_items import (
    SharedTopicsResultsTopicsSegmentsItems,
    SharedTopicsResultsTopicsSegmentsItemsDict,
)


class SharedTopicsResultsTopics(SdkBaseModel):
    segments: Optional[list[SharedTopicsResultsTopicsSegmentsItems]] = UNSET


class SharedTopicsResultsTopicsDict(TypedDict):
    segments: NotRequired[list[SharedTopicsResultsTopicsSegmentsItemsDict]]
