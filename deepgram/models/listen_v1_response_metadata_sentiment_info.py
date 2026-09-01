from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListenV1ResponseMetadataSentimentInfo(SdkBaseModel):
    model_uuid: Optional[str] = UNSET
    input_tokens: Optional[int] = UNSET
    output_tokens: Optional[int] = UNSET


class ListenV1ResponseMetadataSentimentInfoDict(TypedDict):
    model_uuid: NotRequired[str]
    input_tokens: NotRequired[int]
    output_tokens: NotRequired[int]
