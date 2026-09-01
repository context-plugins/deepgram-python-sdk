from __future__ import annotations

from uuid import UUID

from pydantic import EmailStr
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsMember(SdkBaseModel):
    member_id: UUID
    """Unique identifier for the member"""

    email: EmailStr
    """Email address of the member"""


class ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsMemberDict(TypedDict):
    member_id: UUID
    email: EmailStr
