from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersBitRate0(str, Enum):
    """Encoding - mp3(default). Supported bitrates - 32000, 48000(default) bps."""

    _32000 = "32000"
    _48000 = "48000"

    __str__ = str.__str__


V1SpeakPostParametersBitRate0OrStr: TypeAlias = Annotated[
    V1SpeakPostParametersBitRate0 | str, open_enum_validator(V1SpeakPostParametersBitRate0)
]
