from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_project_key_v1_response_item import GetProjectKeyV1ResponseItem, GetProjectKeyV1ResponseItemDict


class GetProjectKeyV1Response(SdkBaseModel):
    item: Optional[GetProjectKeyV1ResponseItem] = UNSET


class GetProjectKeyV1ResponseDict(TypedDict):
    item: NotRequired[GetProjectKeyV1ResponseItem | GetProjectKeyV1ResponseItemDict]
