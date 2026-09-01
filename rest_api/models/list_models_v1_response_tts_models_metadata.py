from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListModelsV1ResponseTtsModelsMetadata(SdkBaseModel):
    accent: Optional[str] = UNSET
    age: Optional[str] = UNSET
    color: Optional[str] = UNSET
    image: Optional[str] = UNSET
    sample: Optional[str] = UNSET
    tags: Optional[list[str]] = UNSET
    use_cases: Optional[list[str]] = UNSET


class ListModelsV1ResponseTtsModelsMetadataDict(TypedDict):
    accent: NotRequired[str]
    age: NotRequired[str]
    color: NotRequired[str]
    image: NotRequired[str]
    sample: NotRequired[str]
    tags: NotRequired[list[str]]
    use_cases: NotRequired[list[str]]
