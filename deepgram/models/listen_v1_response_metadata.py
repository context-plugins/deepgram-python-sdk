from __future__ import annotations

from typing import Any
from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .listen_v1_response_metadata_intents_info import (
    ListenV1ResponseMetadataIntentsInfo,
    ListenV1ResponseMetadataIntentsInfoDict,
)
from .listen_v1_response_metadata_sentiment_info import (
    ListenV1ResponseMetadataSentimentInfo,
    ListenV1ResponseMetadataSentimentInfoDict,
)
from .listen_v1_response_metadata_summary_info import (
    ListenV1ResponseMetadataSummaryInfo,
    ListenV1ResponseMetadataSummaryInfoDict,
)
from .listen_v1_response_metadata_topics_info import (
    ListenV1ResponseMetadataTopicsInfo,
    ListenV1ResponseMetadataTopicsInfoDict,
)


class ListenV1ResponseMetadata(SdkBaseModel):
    transaction_key: str = "deprecated"
    request_id: UUID
    sha256: str
    created: RFC3339DateTime
    duration: float
    channels: int
    models: list[str]
    model_info: Any
    summary_info: Optional[ListenV1ResponseMetadataSummaryInfo] = UNSET
    sentiment_info: Optional[ListenV1ResponseMetadataSentimentInfo] = UNSET
    topics_info: Optional[ListenV1ResponseMetadataTopicsInfo] = UNSET
    intents_info: Optional[ListenV1ResponseMetadataIntentsInfo] = UNSET
    tags: Optional[list[str]] = UNSET


class ListenV1ResponseMetadataDict(TypedDict):
    transaction_key: NotRequired[str]
    request_id: UUID
    sha256: str
    created: RFC3339DateTime
    duration: float
    channels: int
    models: list[str]
    model_info: Any
    summary_info: NotRequired[ListenV1ResponseMetadataSummaryInfoDict]
    sentiment_info: NotRequired[ListenV1ResponseMetadataSentimentInfoDict]
    topics_info: NotRequired[ListenV1ResponseMetadataTopicsInfoDict]
    intents_info: NotRequired[ListenV1ResponseMetadataIntentsInfoDict]
    tags: NotRequired[list[str]]
