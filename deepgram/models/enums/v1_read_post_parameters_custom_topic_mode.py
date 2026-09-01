from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ReadPostParametersCustomTopicMode(str, Enum):
    EXTENDED = "extended"
    STRICT = "strict"

    __str__ = str.__str__


V1ReadPostParametersCustomTopicModeOrStr: TypeAlias = Annotated[
    V1ReadPostParametersCustomTopicMode | str, open_enum_validator(V1ReadPostParametersCustomTopicMode)
]
