from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorResponseLegacyError(SdkBaseModel):
    err_code: Optional[str] = UNSET
    """The error code"""

    err_msg: Optional[str] = UNSET
    """The error message"""

    request_id: Optional[str] = UNSET
    """The request ID"""


class ErrorResponseLegacyErrorDict(TypedDict):
    err_code: NotRequired[str]
    err_msg: NotRequired[str]
    request_id: NotRequired[str]
