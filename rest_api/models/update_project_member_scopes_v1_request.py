from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpdateProjectMemberScopesV1Request(SdkBaseModel):
    scope: str
    """A scope to update"""


class UpdateProjectMemberScopesV1RequestDict(TypedDict):
    scope: str
