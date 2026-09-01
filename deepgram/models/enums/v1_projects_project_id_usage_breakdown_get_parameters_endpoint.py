from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ProjectsProjectIdUsageBreakdownGetParametersEndpoint(str, Enum):
    LISTEN = "listen"
    READ = "read"
    SPEAK = "speak"
    AGENT = "agent"

    __str__ = str.__str__


V1ProjectsProjectIdUsageBreakdownGetParametersEndpointOrStr: TypeAlias = Annotated[
    V1ProjectsProjectIdUsageBreakdownGetParametersEndpoint | str,
    open_enum_validator(V1ProjectsProjectIdUsageBreakdownGetParametersEndpoint),
]
