from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersEncoding1(str, Enum):
    """Encoding - flac. Lossless audio format for high-quality compression."""

    FLAC = "flac"

    __str__ = str.__str__


V1SpeakPostParametersEncoding1OrStr: TypeAlias = Annotated[
    V1SpeakPostParametersEncoding1 | str, open_enum_validator(V1SpeakPostParametersEncoding1)
]
