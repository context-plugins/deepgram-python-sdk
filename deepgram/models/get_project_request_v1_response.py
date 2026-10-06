from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .project_request_response import ProjectRequestResponse, ProjectRequestResponseDict


class GetProjectRequestV1Response(SdkBaseModel):
    request: Optional[ProjectRequestResponse] = UNSET
    """A single request"""


class GetProjectRequestV1ResponseDict(TypedDict):
    request: NotRequired[ProjectRequestResponseDict]
