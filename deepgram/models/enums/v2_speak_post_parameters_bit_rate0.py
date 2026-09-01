from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V2SpeakPostParametersBitRate0(str, Enum):
    """Encoding - mp3(default). Supported bitrates - 8000, 16000, 24000, 32000, 40000, 48000(default) bps."""

    _8000 = "8000"
    _16000 = "16000"
    _24000 = "24000"
    _32000 = "32000"
    _40000 = "40000"
    _48000 = "48000"

    __str__ = str.__str__


V2SpeakPostParametersBitRate0OrStr: TypeAlias = Annotated[
    V2SpeakPostParametersBitRate0 | str, open_enum_validator(V2SpeakPostParametersBitRate0)
]
