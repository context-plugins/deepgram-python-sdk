from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shared_intents_results_intents_segments_items_intents_items import (
    SharedIntentsResultsIntentsSegmentsItemsIntentsItems,
    SharedIntentsResultsIntentsSegmentsItemsIntentsItemsDict,
)


class SharedIntentsResultsIntentsSegmentsItems(SdkBaseModel):
    text: Optional[str] = UNSET
    start_word: Optional[float] = UNSET
    end_word: Optional[float] = UNSET
    intents: Optional[list[SharedIntentsResultsIntentsSegmentsItemsIntentsItems]] = UNSET


class SharedIntentsResultsIntentsSegmentsItemsDict(TypedDict):
    text: NotRequired[str]
    start_word: NotRequired[float]
    end_word: NotRequired[float]
    intents: NotRequired[
        list[
            (
                SharedIntentsResultsIntentsSegmentsItemsIntentsItems
                | SharedIntentsResultsIntentsSegmentsItemsIntentsItemsDict
            )
        ]
    ]
