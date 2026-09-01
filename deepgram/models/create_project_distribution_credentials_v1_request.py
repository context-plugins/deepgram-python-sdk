from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateProjectDistributionCredentialsV1Request(SdkBaseModel):
    """Request body for creating distribution credentials"""

    comment: Optional[str] = UNSET
    """Optional comment about the credentials"""


class CreateProjectDistributionCredentialsV1RequestDict(TypedDict):
    comment: NotRequired[str]
