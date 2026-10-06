from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel


class BillingBreakdownV1ResponseResultsItemsGrouping(SdkBaseModel):
    start: Optional[Date] = UNSET
    """Start date for this group"""

    end: Optional[Date] = UNSET
    """End date for this group"""

    accessor: OptionalNullable[str] = UNSET
    """Optional accessor identifier, null unless grouped by accessor."""

    deployment: OptionalNullable[str] = UNSET
    """Optional deployment identifier, null unless grouped by deployment."""

    line_item: OptionalNullable[str] = UNSET
    """Optional line item identifier, null unless grouped by line item."""

    tags: OptionalNullable[list[str]] = UNSET
    """Optional list of tags, null unless grouped by tags."""


class BillingBreakdownV1ResponseResultsItemsGroupingDict(TypedDict):
    start: NotRequired[Date]
    end: NotRequired[Date]
    accessor: NotRequired[str | None]
    deployment: NotRequired[str | None]
    line_item: NotRequired[str | None]
    tags: NotRequired[list[str] | None]
