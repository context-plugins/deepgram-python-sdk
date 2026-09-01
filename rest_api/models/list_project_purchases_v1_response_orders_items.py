from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ListProjectPurchasesV1ResponseOrdersItems(SdkBaseModel):
    order_id: Optional[UUID] = UNSET
    expiration: Optional[RFC3339DateTime] = UNSET
    created: Optional[RFC3339DateTime] = UNSET
    amount: Optional[float] = UNSET
    units: Optional[str] = UNSET
    order_type: Optional[str] = UNSET


class ListProjectPurchasesV1ResponseOrdersItemsDict(TypedDict):
    order_id: NotRequired[UUID]
    expiration: NotRequired[RFC3339DateTime]
    created: NotRequired[RFC3339DateTime]
    amount: NotRequired[float]
    units: NotRequired[str]
    order_type: NotRequired[str]
