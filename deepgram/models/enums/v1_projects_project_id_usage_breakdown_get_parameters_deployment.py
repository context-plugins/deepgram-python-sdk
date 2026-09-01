from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ProjectsProjectIdUsageBreakdownGetParametersDeployment(str, Enum):
    """Deployment type for the requests"""

    HOSTED = "hosted"
    BETA = "beta"
    SELF_HOSTED = "self-hosted"

    __str__ = str.__str__


V1ProjectsProjectIdUsageBreakdownGetParametersDeploymentOrStr: TypeAlias = Annotated[
    V1ProjectsProjectIdUsageBreakdownGetParametersDeployment | str,
    open_enum_validator(V1ProjectsProjectIdUsageBreakdownGetParametersDeployment),
]
