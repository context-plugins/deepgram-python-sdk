from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .billing_breakdown_v1_response_resolution import (
    BillingBreakdownV1ResponseResolution,
    BillingBreakdownV1ResponseResolutionDict,
)
from .billing_breakdown_v1_response_results_items import (
    BillingBreakdownV1ResponseResultsItems,
    BillingBreakdownV1ResponseResultsItemsDict,
)


class BillingBreakdownV1Response(SdkBaseModel):
    start: Date
    """Start date of the billing summmary period"""

    end: Date
    """End date of the billing summary period"""

    resolution: BillingBreakdownV1ResponseResolution
    results: list[BillingBreakdownV1ResponseResultsItems]


class BillingBreakdownV1ResponseDict(TypedDict):
    start: Date
    end: Date
    resolution: BillingBreakdownV1ResponseResolutionDict
    results: list[BillingBreakdownV1ResponseResultsItemsDict]
