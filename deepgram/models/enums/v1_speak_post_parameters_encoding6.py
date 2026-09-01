from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersEncoding6(str, Enum):
    """Encoding - aac. Advanced audio format offering better quality at smaller file sizes than mp3."""

    AAC = "aac"

    __str__ = str.__str__


V1SpeakPostParametersEncoding6OrStr: TypeAlias = Annotated[
    V1SpeakPostParametersEncoding6 | str, open_enum_validator(V1SpeakPostParametersEncoding6)
]
