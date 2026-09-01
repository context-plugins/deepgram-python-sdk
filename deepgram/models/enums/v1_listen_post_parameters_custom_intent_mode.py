from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ListenPostParametersCustomIntentMode(str, Enum):
    EXTENDED = "extended"
    STRICT = "strict"

    __str__ = str.__str__


V1ListenPostParametersCustomIntentModeOrStr: TypeAlias = Annotated[
    V1ListenPostParametersCustomIntentMode | str, open_enum_validator(V1ListenPostParametersCustomIntentMode)
]
