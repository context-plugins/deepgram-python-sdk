from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProvider(str, Enum):
    QUAY = "quay"

    __str__ = str.__str__


V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProviderOrStr: TypeAlias = Annotated[
    V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProvider | str,
    open_enum_validator(V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProvider),
]
