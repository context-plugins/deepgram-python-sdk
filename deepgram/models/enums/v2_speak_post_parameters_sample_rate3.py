from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V2SpeakPostParametersSampleRate3(str, Enum):
    """Encoding - flac. Supported sample rates - 8000, 16000, 22050, 32000, 48000 Hz."""

    _8000 = "8000"
    _16000 = "16000"
    _22050 = "22050"
    _32000 = "32000"
    _48000 = "48000"

    __str__ = str.__str__


V2SpeakPostParametersSampleRate3OrStr: TypeAlias = Annotated[
    V2SpeakPostParametersSampleRate3 | str, open_enum_validator(V2SpeakPostParametersSampleRate3)
]
