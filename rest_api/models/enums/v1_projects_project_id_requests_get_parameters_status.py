from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ProjectsProjectIdRequestsGetParametersStatus(str, Enum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    __str__ = str.__str__


V1ProjectsProjectIdRequestsGetParametersStatusOrStr: TypeAlias = Annotated[
    V1ProjectsProjectIdRequestsGetParametersStatus | str,
    open_enum_validator(V1ProjectsProjectIdRequestsGetParametersStatus),
]
