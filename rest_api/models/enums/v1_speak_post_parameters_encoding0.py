from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersEncoding0(str, Enum):
    """Encoding - linear16. Uncompressed, high-quality audio format often used for telephony or audio processing."""

    LINEAR16 = "linear16"

    __str__ = str.__str__


V1SpeakPostParametersEncoding0OrStr: TypeAlias = Annotated[
    V1SpeakPostParametersEncoding0 | str, open_enum_validator(V1SpeakPostParametersEncoding0)
]
