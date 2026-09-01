from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel


class UsageBreakdownV1ResponseResultsItemsGrouping(SdkBaseModel):
    start: Optional[Date] = UNSET
    """Start date for this group"""

    end: Optional[Date] = UNSET
    """End date for this group"""

    accessor: OptionalNullable[str] = UNSET
    """Optional accessor identifier"""

    endpoint: OptionalNullable[str] = UNSET
    """Optional endpoint identifier"""

    feature_set: OptionalNullable[str] = UNSET
    """Optional feature set identifier"""

    models: Optional[list[str]] = UNSET
    method: OptionalNullable[str] = UNSET
    """Optional method identifier"""

    tags: Optional[list[str | None]] = UNSET
    """Optional list of tags, null unless grouped by tags."""

    deployment: OptionalNullable[str] = UNSET
    """Optional deployment identifier"""


class UsageBreakdownV1ResponseResultsItemsGroupingDict(TypedDict):
    start: NotRequired[Date]
    end: NotRequired[Date]
    accessor: NotRequired[str | None]
    endpoint: NotRequired[str | None]
    feature_set: NotRequired[str | None]
    models: NotRequired[list[str]]
    method: NotRequired[str | None]
    tags: NotRequired[list[str | None]]
    deployment: NotRequired[str | None]
