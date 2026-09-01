from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_model_v1_response_one_of1_metadata import (
    GetModelV1ResponseOneOf1Metadata,
    GetModelV1ResponseOneOf1MetadataDict,
)


class GetModelV1Response1(SdkBaseModel):
    name: Optional[str] = UNSET
    canonical_name: Optional[str] = UNSET
    architecture: Optional[str] = UNSET
    languages: Optional[list[str]] = UNSET
    version: Optional[str] = UNSET
    uuid: Optional[UUID] = UNSET
    metadata: Optional[GetModelV1ResponseOneOf1Metadata] = UNSET


class GetModelV1Response1Dict(TypedDict):
    name: NotRequired[str]
    canonical_name: NotRequired[str]
    architecture: NotRequired[str]
    languages: NotRequired[list[str]]
    version: NotRequired[str]
    uuid: NotRequired[UUID]
    metadata: NotRequired[GetModelV1ResponseOneOf1Metadata | GetModelV1ResponseOneOf1MetadataDict]
