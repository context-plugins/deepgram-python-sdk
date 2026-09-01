from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateProjectInviteV1Request(SdkBaseModel):
    """Request body for creating a project invite"""

    email: str
    """The email address of the invitee"""

    scope: str
    """The scope of the invitee"""


class CreateProjectInviteV1RequestDict(TypedDict):
    email: str
    scope: str
