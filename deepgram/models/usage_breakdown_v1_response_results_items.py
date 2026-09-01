from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .usage_breakdown_v1_response_results_items_grouping import (
    UsageBreakdownV1ResponseResultsItemsGrouping,
    UsageBreakdownV1ResponseResultsItemsGroupingDict,
)


class UsageBreakdownV1ResponseResultsItems(SdkBaseModel):
    hours: float
    """Audio hours processed"""

    total_hours: float
    """Total hours including all processing"""

    agent_hours: float
    """Agent hours used"""

    tokens_in: float
    """Number of input tokens"""

    tokens_out: float
    """Number of output tokens"""

    tts_characters: float
    """Number of text-to-speech characters processed"""

    requests: float
    """Number of requests"""

    grouping: UsageBreakdownV1ResponseResultsItemsGrouping


class UsageBreakdownV1ResponseResultsItemsDict(TypedDict):
    hours: float
    total_hours: float
    agent_hours: float
    tokens_in: float
    tokens_out: float
    tts_characters: float
    requests: float
    grouping: UsageBreakdownV1ResponseResultsItemsGrouping | UsageBreakdownV1ResponseResultsItemsGroupingDict
