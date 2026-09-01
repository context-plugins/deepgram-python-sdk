from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .usage_breakdown_v1_response_resolution import (
    UsageBreakdownV1ResponseResolution,
    UsageBreakdownV1ResponseResolutionDict,
)
from .usage_breakdown_v1_response_results_items import (
    UsageBreakdownV1ResponseResultsItems,
    UsageBreakdownV1ResponseResultsItemsDict,
)


class UsageBreakdownV1Response(SdkBaseModel):
    start: Date
    """Start date of the usage period"""

    end: Date
    """End date of the usage period"""

    resolution: UsageBreakdownV1ResponseResolution
    results: list[UsageBreakdownV1ResponseResultsItems]


class UsageBreakdownV1ResponseDict(TypedDict):
    start: Date
    end: Date
    resolution: UsageBreakdownV1ResponseResolution | UsageBreakdownV1ResponseResolutionDict
    results: list[UsageBreakdownV1ResponseResultsItems | UsageBreakdownV1ResponseResultsItemsDict]
