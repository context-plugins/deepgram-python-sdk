from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersSampleRate3(str, Enum):
    """Encoding - mp3. Sample rate is fixed and not configurable (22050 Hz)."""

    _22050 = "22050"

    __str__ = str.__str__


V1SpeakPostParametersSampleRate3OrStr: TypeAlias = Annotated[
    V1SpeakPostParametersSampleRate3 | str, open_enum_validator(V1SpeakPostParametersSampleRate3)
]
