from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersContainer3(str, Enum):
    """Encoding - alaw. Supported container - wav (default), or no container."""

    WAV = "wav"

    __str__ = str.__str__


V1SpeakPostParametersContainer3OrStr: TypeAlias = Annotated[
    V1SpeakPostParametersContainer3 | str, open_enum_validator(V1SpeakPostParametersContainer3)
]
