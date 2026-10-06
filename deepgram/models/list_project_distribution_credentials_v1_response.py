from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_project_distribution_credentials_v1_response_distribution_credentials_items import (
    ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItems,
    ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsDict,
)


class ListProjectDistributionCredentialsV1Response(SdkBaseModel):
    distribution_credentials: Optional[
        list[ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItems]
    ] = UNSET
    """Array of distribution credentials with associated member information"""


class ListProjectDistributionCredentialsV1ResponseDict(TypedDict):
    distribution_credentials: NotRequired[
        list[ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsDict]
    ]
