from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_project_distribution_credentials_v1_response_distribution_credentials import (
    CreateProjectDistributionCredentialsV1ResponseDistributionCredentials,
    CreateProjectDistributionCredentialsV1ResponseDistributionCredentialsDict,
)
from .create_project_distribution_credentials_v1_response_member import (
    CreateProjectDistributionCredentialsV1ResponseMember,
    CreateProjectDistributionCredentialsV1ResponseMemberDict,
)


class CreateProjectDistributionCredentialsV1Response(SdkBaseModel):
    member: CreateProjectDistributionCredentialsV1ResponseMember
    distribution_credentials: CreateProjectDistributionCredentialsV1ResponseDistributionCredentials


class CreateProjectDistributionCredentialsV1ResponseDict(TypedDict):
    member: (
        CreateProjectDistributionCredentialsV1ResponseMember | CreateProjectDistributionCredentialsV1ResponseMemberDict
    )
    distribution_credentials: (
        CreateProjectDistributionCredentialsV1ResponseDistributionCredentials
        | CreateProjectDistributionCredentialsV1ResponseDistributionCredentialsDict
    )
