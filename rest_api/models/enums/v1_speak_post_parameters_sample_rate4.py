from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersSampleRate4(str, Enum):
    """Encoding - opus. Sample rate is fixed at 48000 Hz."""

    _48000 = "48000"

    __str__ = str.__str__


V1SpeakPostParametersSampleRate4OrStr: TypeAlias = Annotated[
    V1SpeakPostParametersSampleRate4 | str, open_enum_validator(V1SpeakPostParametersSampleRate4)
]
