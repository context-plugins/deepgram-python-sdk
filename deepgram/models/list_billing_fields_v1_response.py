from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.list_billing_fields_v1_response_deployments_items import ListBillingFieldsV1ResponseDeploymentsItemsOrStr


class ListBillingFieldsV1Response(SdkBaseModel):
    accessors: Optional[list[UUID]] = UNSET
    """List of accessor UUIDs for the time period"""

    deployments: Optional[list[ListBillingFieldsV1ResponseDeploymentsItemsOrStr]] = UNSET
    """List of deployment types for the time period"""

    tags: Optional[list[str]] = UNSET
    """List of tags for the time period"""

    line_items: Optional[dict[str, str]] = UNSET
    """Map of line item names to human-readable descriptions for the time period"""


class ListBillingFieldsV1ResponseDict(TypedDict):
    accessors: NotRequired[list[UUID]]
    deployments: NotRequired[list[ListBillingFieldsV1ResponseDeploymentsItemsOrStr]]
    tags: NotRequired[list[str]]
    line_items: NotRequired[dict[str, str]]
