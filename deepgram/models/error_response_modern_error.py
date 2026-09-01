from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorResponseModernError(SdkBaseModel):
    category: Optional[str] = UNSET
    """The category of the error"""

    message: Optional[str] = UNSET
    """A message about the error"""

    details: Optional[str] = UNSET
    """A description of the error"""

    request_id: Optional[str] = UNSET
    """The unique identifier of the request"""


class ErrorResponseModernErrorDict(TypedDict):
    category: NotRequired[str]
    message: NotRequired[str]
    details: NotRequired[str]
    request_id: NotRequired[str]
