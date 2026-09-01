from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BillingBreakdownV1ResponseResolution(SdkBaseModel):
    units: str
    """Time unit for the resolution"""

    amount: float
    """Amount of units"""


class BillingBreakdownV1ResponseResolutionDict(TypedDict):
    units: str
    amount: float
