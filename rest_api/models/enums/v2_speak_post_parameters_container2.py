from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V2SpeakPostParametersContainer2(str, Enum):
    """Encoding - mulaw. Supported container - wav (default), or no container."""

    WAV = "wav"

    __str__ = str.__str__


V2SpeakPostParametersContainer2OrStr: TypeAlias = Annotated[
    V2SpeakPostParametersContainer2 | str, open_enum_validator(V2SpeakPostParametersContainer2)
]
