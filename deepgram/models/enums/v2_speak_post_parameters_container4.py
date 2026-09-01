from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V2SpeakPostParametersContainer4(str, Enum):
    """Encoding - opus. Supported container - ogg (default)."""

    OGG = "ogg"

    __str__ = str.__str__


V2SpeakPostParametersContainer4OrStr: TypeAlias = Annotated[
    V2SpeakPostParametersContainer4 | str, open_enum_validator(V2SpeakPostParametersContainer4)
]
