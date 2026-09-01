from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .read_v1_response_metadata import ReadV1ResponseMetadata, ReadV1ResponseMetadataDict
from .read_v1_response_results import ReadV1ResponseResults, ReadV1ResponseResultsDict


class ReadV1Response(SdkBaseModel):
    """The standard text response"""

    metadata: ReadV1ResponseMetadata
    results: ReadV1ResponseResults


class ReadV1ResponseDict(TypedDict):
    metadata: ReadV1ResponseMetadata | ReadV1ResponseMetadataDict
    results: ReadV1ResponseResults | ReadV1ResponseResultsDict
