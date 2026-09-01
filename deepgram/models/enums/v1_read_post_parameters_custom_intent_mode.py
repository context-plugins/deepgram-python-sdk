from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ReadPostParametersCustomIntentMode(str, Enum):
    EXTENDED = "extended"
    STRICT = "strict"

    __str__ = str.__str__


V1ReadPostParametersCustomIntentModeOrStr: TypeAlias = Annotated[
    V1ReadPostParametersCustomIntentMode | str, open_enum_validator(V1ReadPostParametersCustomIntentMode)
]
