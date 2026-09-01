from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ProjectsProjectIdUsageGetParametersMethod(str, Enum):
    """Method type for the request"""

    SYNC = "sync"
    ASYNC = "async"
    STREAMING = "streaming"

    __str__ = str.__str__


V1ProjectsProjectIdUsageGetParametersMethodOrStr: TypeAlias = Annotated[
    V1ProjectsProjectIdUsageGetParametersMethod | str, open_enum_validator(V1ProjectsProjectIdUsageGetParametersMethod)
]
