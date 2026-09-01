from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_project_purchases_v1_response_orders_items import (
    ListProjectPurchasesV1ResponseOrdersItems,
    ListProjectPurchasesV1ResponseOrdersItemsDict,
)


class ListProjectPurchasesV1Response(SdkBaseModel):
    orders: Optional[list[ListProjectPurchasesV1ResponseOrdersItems]] = UNSET


class ListProjectPurchasesV1ResponseDict(TypedDict):
    orders: NotRequired[list[ListProjectPurchasesV1ResponseOrdersItems | ListProjectPurchasesV1ResponseOrdersItemsDict]]
