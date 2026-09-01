from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListenV1ResponseMetadataSummaryInfo(SdkBaseModel):
    model_uuid: Optional[str] = UNSET
    input_tokens: Optional[int] = UNSET
    output_tokens: Optional[int] = UNSET


class ListenV1ResponseMetadataSummaryInfoDict(TypedDict):
    model_uuid: NotRequired[str]
    input_tokens: NotRequired[int]
    output_tokens: NotRequired[int]
