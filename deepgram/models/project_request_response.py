from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ProjectRequestResponse(SdkBaseModel):
    """A single request"""

    request_id: Optional[str] = UNSET
    """The unique identifier of the request"""

    project_uuid: Optional[str] = UNSET
    """The unique identifier of the project"""

    created: Optional[RFC3339DateTime] = UNSET
    """The date and time the request was created"""

    path: Optional[str] = UNSET
    """The API path of the request"""

    api_key_id: Optional[str] = UNSET
    """The unique identifier of the API key"""

    response: Optional[Any] = UNSET
    """The response of the request"""

    code: Optional[float] = UNSET
    """The response code of the request"""

    deployment: Optional[str] = UNSET
    """The deployment type"""

    callback: Optional[str] = UNSET
    """The callback URL for the request"""


class ProjectRequestResponseDict(TypedDict):
    request_id: NotRequired[str]
    project_uuid: NotRequired[str]
    created: NotRequired[RFC3339DateTime]
    path: NotRequired[str]
    api_key_id: NotRequired[str]
    response: NotRequired[Any]
    code: NotRequired[float]
    deployment: NotRequired[str]
    callback: NotRequired[str]
