from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shared_intents_results_intents import SharedIntentsResultsIntents, SharedIntentsResultsIntentsDict


class SharedIntentsResults(SdkBaseModel):
    intents: Optional[SharedIntentsResultsIntents] = UNSET


class SharedIntentsResultsDict(TypedDict):
    intents: NotRequired[SharedIntentsResultsIntentsDict]
