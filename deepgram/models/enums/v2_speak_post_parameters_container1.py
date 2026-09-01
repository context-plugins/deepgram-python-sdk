from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V2SpeakPostParametersContainer1(str, Enum):
    """Encoding - linear16. Supported container - wav (default), or no container."""

    WAV = "wav"

    __str__ = str.__str__


V2SpeakPostParametersContainer1OrStr: TypeAlias = Annotated[
    V2SpeakPostParametersContainer1 | str, open_enum_validator(V2SpeakPostParametersContainer1)
]
