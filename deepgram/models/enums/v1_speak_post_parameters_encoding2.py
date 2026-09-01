from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersEncoding2(str, Enum):
    """Encoding - mulaw. Compressed audio format commonly used in telephony."""

    MULAW = "mulaw"

    __str__ = str.__str__


V1SpeakPostParametersEncoding2OrStr: TypeAlias = Annotated[
    V1SpeakPostParametersEncoding2 | str, open_enum_validator(V1SpeakPostParametersEncoding2)
]
