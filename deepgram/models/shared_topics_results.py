from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shared_topics_results_topics import SharedTopicsResultsTopics, SharedTopicsResultsTopicsDict


class SharedTopicsResults(SdkBaseModel):
    topics: Optional[SharedTopicsResultsTopics] = UNSET


class SharedTopicsResultsDict(TypedDict):
    topics: NotRequired[SharedTopicsResultsTopics | SharedTopicsResultsTopicsDict]
