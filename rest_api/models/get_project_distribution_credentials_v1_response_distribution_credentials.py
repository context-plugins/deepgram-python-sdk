from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class GetProjectDistributionCredentialsV1ResponseDistributionCredentials(SdkBaseModel):
    distribution_credentials_id: UUID
    """Unique identifier for the distribution credentials"""

    provider: str
    """The provider of the distribution service"""

    comment: Optional[str] = UNSET
    """Optional comment about the credentials"""

    scopes: list[str]
    """List of permission scopes for the credentials"""

    created: RFC3339DateTime
    """Timestamp when the credentials were created"""


class GetProjectDistributionCredentialsV1ResponseDistributionCredentialsDict(TypedDict):
    distribution_credentials_id: UUID
    provider: str
    comment: NotRequired[str]
    scopes: list[str]
    created: RFC3339DateTime
