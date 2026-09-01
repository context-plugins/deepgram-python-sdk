from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .listen_v1_response_metadata import ListenV1ResponseMetadata, ListenV1ResponseMetadataDict
from .listen_v1_response_results import ListenV1ResponseResults, ListenV1ResponseResultsDict


class ListenV1ResponseError(SdkBaseModel):
    """The standard transcription response"""

    metadata: ListenV1ResponseMetadata
    results: ListenV1ResponseResults


class ListenV1ResponseErrorDict(TypedDict):
    metadata: ListenV1ResponseMetadata | ListenV1ResponseMetadataDict
    results: ListenV1ResponseResults | ListenV1ResponseResultsDict
