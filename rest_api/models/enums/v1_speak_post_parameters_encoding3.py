from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersEncoding3(str, Enum):
    """Encoding - alaw. Similar to mulaw but used in international telephony."""

    ALAW = "alaw"

    __str__ = str.__str__


V1SpeakPostParametersEncoding3OrStr: TypeAlias = Annotated[
    V1SpeakPostParametersEncoding3 | str, open_enum_validator(V1SpeakPostParametersEncoding3)
]
