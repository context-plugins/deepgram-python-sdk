from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shared_topics_results import SharedTopicsResults, SharedTopicsResultsDict


class SharedTopics(SdkBaseModel):
    """Output whenever ``topics=true`` is used"""

    results: Optional[SharedTopicsResults] = UNSET


class SharedTopicsDict(TypedDict):
    results: NotRequired[SharedTopicsResultsDict]
