from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GetProjectV1Response(SdkBaseModel):
    project_id: Optional[str] = UNSET
    """The unique identifier of the project"""

    mip_opt_out: Optional[bool] = UNSET
    """Model Improvement Program opt-out"""

    name: Optional[str] = UNSET
    """The name of the project"""


class GetProjectV1ResponseDict(TypedDict):
    project_id: NotRequired[str]
    mip_opt_out: NotRequired[bool]
    name: NotRequired[str]
