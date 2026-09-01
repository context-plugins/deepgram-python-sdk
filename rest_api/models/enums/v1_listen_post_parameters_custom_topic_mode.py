from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ListenPostParametersCustomTopicMode(str, Enum):
    EXTENDED = "extended"
    STRICT = "strict"

    __str__ = str.__str__


V1ListenPostParametersCustomTopicModeOrStr: TypeAlias = Annotated[
    V1ListenPostParametersCustomTopicMode | str, open_enum_validator(V1ListenPostParametersCustomTopicMode)
]
