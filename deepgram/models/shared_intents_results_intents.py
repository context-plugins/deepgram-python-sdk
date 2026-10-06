from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shared_intents_results_intents_segments_items import (
    SharedIntentsResultsIntentsSegmentsItems,
    SharedIntentsResultsIntentsSegmentsItemsDict,
)


class SharedIntentsResultsIntents(SdkBaseModel):
    segments: Optional[list[SharedIntentsResultsIntentsSegmentsItems]] = UNSET


class SharedIntentsResultsIntentsDict(TypedDict):
    segments: NotRequired[list[SharedIntentsResultsIntentsSegmentsItemsDict]]
