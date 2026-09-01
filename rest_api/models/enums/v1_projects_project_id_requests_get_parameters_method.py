from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ProjectsProjectIdRequestsGetParametersMethod(str, Enum):
    """Method type for the request"""

    SYNC = "sync"
    ASYNC = "async"
    STREAMING = "streaming"

    __str__ = str.__str__


V1ProjectsProjectIdRequestsGetParametersMethodOrStr: TypeAlias = Annotated[
    V1ProjectsProjectIdRequestsGetParametersMethod | str,
    open_enum_validator(V1ProjectsProjectIdRequestsGetParametersMethod),
]
