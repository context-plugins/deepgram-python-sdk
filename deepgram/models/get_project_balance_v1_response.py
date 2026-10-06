from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GetProjectBalanceV1Response(SdkBaseModel):
    balance_id: Optional[str] = UNSET
    """The unique identifier of the balance"""

    amount: float = 0.0
    """The amount of the balance"""

    units: Optional[str] = UNSET
    """The units of the balance, such as "USD"
    """

    purchase_order_id: Optional[str] = UNSET
    """Description or reference of the purchase"""


class GetProjectBalanceV1ResponseDict(TypedDict):
    balance_id: NotRequired[str]
    amount: NotRequired[float]
    units: NotRequired[str]
    purchase_order_id: NotRequired[str]
