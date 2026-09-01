from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdateProjectV1Request(SdkBaseModel):
    name: Optional[str] = UNSET
    """The name of the project"""


class UpdateProjectV1RequestDict(TypedDict):
    name: NotRequired[str]
