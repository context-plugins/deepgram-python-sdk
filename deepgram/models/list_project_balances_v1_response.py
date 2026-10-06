from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_project_balances_v1_response_balances_items import (
    ListProjectBalancesV1ResponseBalancesItems,
    ListProjectBalancesV1ResponseBalancesItemsDict,
)


class ListProjectBalancesV1Response(SdkBaseModel):
    balances: Optional[list[ListProjectBalancesV1ResponseBalancesItems]] = UNSET


class ListProjectBalancesV1ResponseDict(TypedDict):
    balances: NotRequired[list[ListProjectBalancesV1ResponseBalancesItemsDict]]
