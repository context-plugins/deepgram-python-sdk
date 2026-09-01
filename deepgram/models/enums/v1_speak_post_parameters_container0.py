from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersContainer0(str, Enum):
    """No container."""

    NONE = "none"

    __str__ = str.__str__


V1SpeakPostParametersContainer0OrStr: TypeAlias = Annotated[
    V1SpeakPostParametersContainer0 | str, open_enum_validator(V1SpeakPostParametersContainer0)
]
