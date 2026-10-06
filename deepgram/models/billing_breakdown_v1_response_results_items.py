from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .billing_breakdown_v1_response_results_items_grouping import (
    BillingBreakdownV1ResponseResultsItemsGrouping,
    BillingBreakdownV1ResponseResultsItemsGroupingDict,
)


class BillingBreakdownV1ResponseResultsItems(SdkBaseModel):
    dollars: float
    """USD cost of the billing for this grouping"""

    grouping: BillingBreakdownV1ResponseResultsItemsGrouping


class BillingBreakdownV1ResponseResultsItemsDict(TypedDict):
    dollars: float
    grouping: BillingBreakdownV1ResponseResultsItemsGroupingDict
