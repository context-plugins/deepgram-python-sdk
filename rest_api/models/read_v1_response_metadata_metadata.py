from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .read_v1_response_metadata_metadata_intents_info import (
    ReadV1ResponseMetadataMetadataIntentsInfo,
    ReadV1ResponseMetadataMetadataIntentsInfoDict,
)
from .read_v1_response_metadata_metadata_sentiment_info import (
    ReadV1ResponseMetadataMetadataSentimentInfo,
    ReadV1ResponseMetadataMetadataSentimentInfoDict,
)
from .read_v1_response_metadata_metadata_summary_info import (
    ReadV1ResponseMetadataMetadataSummaryInfo,
    ReadV1ResponseMetadataMetadataSummaryInfoDict,
)
from .read_v1_response_metadata_metadata_topics_info import (
    ReadV1ResponseMetadataMetadataTopicsInfo,
    ReadV1ResponseMetadataMetadataTopicsInfoDict,
)


class ReadV1ResponseMetadataMetadata(SdkBaseModel):
    request_id: Optional[UUID] = UNSET
    created: Optional[RFC3339DateTime] = UNSET
    language: Optional[str] = UNSET
    summary_info: Optional[ReadV1ResponseMetadataMetadataSummaryInfo] = UNSET
    sentiment_info: Optional[ReadV1ResponseMetadataMetadataSentimentInfo] = UNSET
    topics_info: Optional[ReadV1ResponseMetadataMetadataTopicsInfo] = UNSET
    intents_info: Optional[ReadV1ResponseMetadataMetadataIntentsInfo] = UNSET


class ReadV1ResponseMetadataMetadataDict(TypedDict):
    request_id: NotRequired[UUID]
    created: NotRequired[RFC3339DateTime]
    language: NotRequired[str]
    summary_info: NotRequired[ReadV1ResponseMetadataMetadataSummaryInfo | ReadV1ResponseMetadataMetadataSummaryInfoDict]
    sentiment_info: NotRequired[
        ReadV1ResponseMetadataMetadataSentimentInfo | ReadV1ResponseMetadataMetadataSentimentInfoDict
    ]
    topics_info: NotRequired[ReadV1ResponseMetadataMetadataTopicsInfo | ReadV1ResponseMetadataMetadataTopicsInfoDict]
    intents_info: NotRequired[ReadV1ResponseMetadataMetadataIntentsInfo | ReadV1ResponseMetadataMetadataIntentsInfoDict]
