from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shared_intents_results import SharedIntentsResults, SharedIntentsResultsDict


class SharedIntents(SdkBaseModel):
    """Output whenever ``intents=true`` is used"""

    results: Optional[SharedIntentsResults] = UNSET


class SharedIntentsDict(TypedDict):
    results: NotRequired[SharedIntentsResults | SharedIntentsResultsDict]
