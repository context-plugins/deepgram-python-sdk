from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsageBreakdownV1ResponseResolution(SdkBaseModel):
    units: str
    """Time unit for the resolution"""

    amount: float
    """Amount of units"""


class UsageBreakdownV1ResponseResolutionDict(TypedDict):
    units: str
    amount: float
