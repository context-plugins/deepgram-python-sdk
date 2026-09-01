from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .get_project_distribution_credentials_v1_response_distribution_credentials import (
    GetProjectDistributionCredentialsV1ResponseDistributionCredentials,
    GetProjectDistributionCredentialsV1ResponseDistributionCredentialsDict,
)
from .get_project_distribution_credentials_v1_response_member import (
    GetProjectDistributionCredentialsV1ResponseMember,
    GetProjectDistributionCredentialsV1ResponseMemberDict,
)


class GetProjectDistributionCredentialsV1Response(SdkBaseModel):
    member: GetProjectDistributionCredentialsV1ResponseMember
    distribution_credentials: GetProjectDistributionCredentialsV1ResponseDistributionCredentials


class GetProjectDistributionCredentialsV1ResponseDict(TypedDict):
    member: GetProjectDistributionCredentialsV1ResponseMember | GetProjectDistributionCredentialsV1ResponseMemberDict
    distribution_credentials: (
        GetProjectDistributionCredentialsV1ResponseDistributionCredentials
        | GetProjectDistributionCredentialsV1ResponseDistributionCredentialsDict
    )
