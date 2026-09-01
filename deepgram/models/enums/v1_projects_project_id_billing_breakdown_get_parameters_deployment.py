from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ProjectsProjectIdBillingBreakdownGetParametersDeployment(str, Enum):
    """Deployment type for the requests"""

    HOSTED = "hosted"
    BETA = "beta"
    SELF_HOSTED = "self-hosted"

    __str__ = str.__str__


V1ProjectsProjectIdBillingBreakdownGetParametersDeploymentOrStr: TypeAlias = Annotated[
    V1ProjectsProjectIdBillingBreakdownGetParametersDeployment | str,
    open_enum_validator(V1ProjectsProjectIdBillingBreakdownGetParametersDeployment),
]
