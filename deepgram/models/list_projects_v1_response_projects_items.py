from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListProjectsV1ResponseProjectsItems(SdkBaseModel):
    project_id: Optional[str] = UNSET
    """The unique identifier of the project"""

    name: Optional[str] = UNSET
    """The name of the project"""


class ListProjectsV1ResponseProjectsItemsDict(TypedDict):
    project_id: NotRequired[str]
    name: NotRequired[str]
