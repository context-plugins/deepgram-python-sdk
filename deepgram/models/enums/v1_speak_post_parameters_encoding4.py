from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersEncoding4(str, Enum):
    """Encoding - mp3. Popular compressed audio format for music and streaming."""

    MP3 = "mp3"

    __str__ = str.__str__


V1SpeakPostParametersEncoding4OrStr: TypeAlias = Annotated[
    V1SpeakPostParametersEncoding4 | str, open_enum_validator(V1SpeakPostParametersEncoding4)
]
