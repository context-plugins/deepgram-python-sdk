from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_models_v1_response_tts_models_metadata import (
    ListModelsV1ResponseTtsModelsMetadata,
    ListModelsV1ResponseTtsModelsMetadataDict,
)


class ListModelsV1ResponseTtsModels(SdkBaseModel):
    name: Optional[str] = UNSET
    canonical_name: Optional[str] = UNSET
    architecture: Optional[str] = UNSET
    languages: Optional[list[str]] = UNSET
    version: Optional[str] = UNSET
    uuid: Optional[UUID] = UNSET
    metadata: Optional[ListModelsV1ResponseTtsModelsMetadata] = UNSET


class ListModelsV1ResponseTtsModelsDict(TypedDict):
    name: NotRequired[str]
    canonical_name: NotRequired[str]
    architecture: NotRequired[str]
    languages: NotRequired[list[str]]
    version: NotRequired[str]
    uuid: NotRequired[UUID]
    metadata: NotRequired[ListModelsV1ResponseTtsModelsMetadataDict]
