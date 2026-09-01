from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V2SpeakPostParametersPriority(str, Enum):
    LOW = "low"

    __str__ = str.__str__


V2SpeakPostParametersPriorityOrStr: TypeAlias = Annotated[
    V2SpeakPostParametersPriority | str, open_enum_validator(V2SpeakPostParametersPriority)
]
