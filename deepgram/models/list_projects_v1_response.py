from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_projects_v1_response_projects_items import (
    ListProjectsV1ResponseProjectsItems,
    ListProjectsV1ResponseProjectsItemsDict,
)


class ListProjectsV1Response(SdkBaseModel):
    projects: Optional[list[ListProjectsV1ResponseProjectsItems]] = UNSET


class ListProjectsV1ResponseDict(TypedDict):
    projects: NotRequired[list[ListProjectsV1ResponseProjectsItems | ListProjectsV1ResponseProjectsItemsDict]]
