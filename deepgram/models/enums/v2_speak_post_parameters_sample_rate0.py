from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V2SpeakPostParametersSampleRate0(str, Enum):
    """Encoding - linear16. Supported sample rates - 8000, 16000, 24000, 32000, 44100, 48000 Hz."""

    _8000 = "8000"
    _16000 = "16000"
    _24000 = "24000"
    _32000 = "32000"
    _44100 = "44100"
    _48000 = "48000"

    __str__ = str.__str__


V2SpeakPostParametersSampleRate0OrStr: TypeAlias = Annotated[
    V2SpeakPostParametersSampleRate0 | str, open_enum_validator(V2SpeakPostParametersSampleRate0)
]
