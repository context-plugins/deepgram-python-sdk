from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ProjectsProjectIdRequestsGetParametersEndpoint(str, Enum):
    LISTEN = "listen"
    READ = "read"
    SPEAK = "speak"
    AGENT = "agent"

    __str__ = str.__str__


V1ProjectsProjectIdRequestsGetParametersEndpointOrStr: TypeAlias = Annotated[
    V1ProjectsProjectIdRequestsGetParametersEndpoint | str,
    open_enum_validator(V1ProjectsProjectIdRequestsGetParametersEndpoint),
]
