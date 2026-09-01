from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeleteProjectKeyV1Response(SdkBaseModel):
    message: Optional[str] = UNSET


class DeleteProjectKeyV1ResponseDict(TypedDict):
    message: NotRequired[str]
