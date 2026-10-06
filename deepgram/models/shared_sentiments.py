from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shared_sentiments_average import SharedSentimentsAverage, SharedSentimentsAverageDict
from .shared_sentiments_segments_items import SharedSentimentsSegmentsItems, SharedSentimentsSegmentsItemsDict


class SharedSentiments(SdkBaseModel):
    """Output whenever ``sentiment=true`` is used"""

    segments: Optional[list[SharedSentimentsSegmentsItems]] = UNSET
    average: Optional[SharedSentimentsAverage] = UNSET


class SharedSentimentsDict(TypedDict):
    segments: NotRequired[list[SharedSentimentsSegmentsItemsDict]]
    average: NotRequired[SharedSentimentsAverageDict]
