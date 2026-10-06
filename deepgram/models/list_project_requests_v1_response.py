from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .project_request_response import ProjectRequestResponse, ProjectRequestResponseDict


class ListProjectRequestsV1Response(SdkBaseModel):
    page: Optional[float] = UNSET
    """The page number of the paginated response"""

    limit: Optional[float] = UNSET
    """The number of results per page"""

    requests: Optional[list[ProjectRequestResponse]] = UNSET


class ListProjectRequestsV1ResponseDict(TypedDict):
    page: NotRequired[float]
    limit: NotRequired[float]
    requests: NotRequired[list[ProjectRequestResponseDict]]
