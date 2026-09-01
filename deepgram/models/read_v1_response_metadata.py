from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .read_v1_response_metadata_metadata import ReadV1ResponseMetadataMetadata, ReadV1ResponseMetadataMetadataDict


class ReadV1ResponseMetadata(SdkBaseModel):
    metadata: Optional[ReadV1ResponseMetadataMetadata] = UNSET


class ReadV1ResponseMetadataDict(TypedDict):
    metadata: NotRequired[ReadV1ResponseMetadataMetadata | ReadV1ResponseMetadataMetadataDict]
