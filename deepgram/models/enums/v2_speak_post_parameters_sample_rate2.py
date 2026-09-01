from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V2SpeakPostParametersSampleRate2(str, Enum):
    """Encoding - alaw. Supported sample rates - 8000, 16000 Hz."""

    _8000 = "8000"
    _16000 = "16000"

    __str__ = str.__str__


V2SpeakPostParametersSampleRate2OrStr: TypeAlias = Annotated[
    V2SpeakPostParametersSampleRate2 | str, open_enum_validator(V2SpeakPostParametersSampleRate2)
]
