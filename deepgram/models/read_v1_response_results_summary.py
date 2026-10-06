from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .read_v1_response_results_summary_results import (
    ReadV1ResponseResultsSummaryResults,
    ReadV1ResponseResultsSummaryResultsDict,
)


class ReadV1ResponseResultsSummary(SdkBaseModel):
    """Output whenever ``summary=true`` is used"""

    results: Optional[ReadV1ResponseResultsSummaryResults] = UNSET


class ReadV1ResponseResultsSummaryDict(TypedDict):
    results: NotRequired[ReadV1ResponseResultsSummaryResultsDict]
