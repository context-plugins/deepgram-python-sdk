from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(SdkBaseModel):
    text: Optional[str] = UNSET
    start: Optional[float] = UNSET
    end: Optional[float] = UNSET


class ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItemsDict(TypedDict):
    text: NotRequired[str]
    start: NotRequired[float]
    end: NotRequired[float]
