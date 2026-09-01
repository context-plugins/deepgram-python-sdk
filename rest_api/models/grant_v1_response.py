from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GrantV1Response(SdkBaseModel):
    access_token: str
    """JSON Web Token (JWT)"""

    expires_in: Optional[float] = UNSET
    """Time in seconds until the JWT expires"""


class GrantV1ResponseDict(TypedDict):
    access_token: str
    expires_in: NotRequired[float]
