from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GetModelV1Response0(SdkBaseModel):
    name: Optional[str] = UNSET
    canonical_name: Optional[str] = UNSET
    architecture: Optional[str] = UNSET
    languages: Optional[list[str]] = UNSET
    version: Optional[str] = UNSET
    uuid: Optional[UUID] = UNSET
    batch: Optional[bool] = UNSET
    streaming: Optional[bool] = UNSET
    formatted_output: Optional[bool] = UNSET


class GetModelV1Response0Dict(TypedDict):
    name: NotRequired[str]
    canonical_name: NotRequired[str]
    architecture: NotRequired[str]
    languages: NotRequired[list[str]]
    version: NotRequired[str]
    uuid: NotRequired[UUID]
    batch: NotRequired[bool]
    streaming: NotRequired[bool]
    formatted_output: NotRequired[bool]
