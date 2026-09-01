from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersSampleRate1(str, Enum):
    """Encoding - mulaw. Supported sample rates - 8000, 16000 Hz."""

    _8000 = "8000"
    _16000 = "16000"

    __str__ = str.__str__


V1SpeakPostParametersSampleRate1OrStr: TypeAlias = Annotated[
    V1SpeakPostParametersSampleRate1 | str, open_enum_validator(V1SpeakPostParametersSampleRate1)
]
