from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .read_v1_response_results_summary_results_summary import (
    ReadV1ResponseResultsSummaryResultsSummary,
    ReadV1ResponseResultsSummaryResultsSummaryDict,
)


class ReadV1ResponseResultsSummaryResults(SdkBaseModel):
    summary: Optional[ReadV1ResponseResultsSummaryResultsSummary] = UNSET


class ReadV1ResponseResultsSummaryResultsDict(TypedDict):
    summary: NotRequired[ReadV1ResponseResultsSummaryResultsSummary | ReadV1ResponseResultsSummaryResultsSummaryDict]
