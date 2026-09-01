from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V2SpeakPostParametersEncoding5(str, Enum):
    """Encoding - opus. High-compression audio format optimized for real-time communications."""

    OPUS = "opus"

    __str__ = str.__str__


V2SpeakPostParametersEncoding5OrStr: TypeAlias = Annotated[
    V2SpeakPostParametersEncoding5 | str, open_enum_validator(V2SpeakPostParametersEncoding5)
]
