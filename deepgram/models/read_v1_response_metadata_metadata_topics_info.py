from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReadV1ResponseMetadataMetadataTopicsInfo(SdkBaseModel):
    model_uuid: Optional[UUID] = UNSET
    input_tokens: Optional[int] = UNSET
    output_tokens: Optional[int] = UNSET


class ReadV1ResponseMetadataMetadataTopicsInfoDict(TypedDict):
    model_uuid: NotRequired[UUID]
    input_tokens: NotRequired[int]
    output_tokens: NotRequired[int]
