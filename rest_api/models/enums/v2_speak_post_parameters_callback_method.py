from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V2SpeakPostParametersCallbackMethod(str, Enum):
    POST = "POST"
    PUT = "PUT"

    __str__ = str.__str__


V2SpeakPostParametersCallbackMethodOrStr: TypeAlias = Annotated[
    V2SpeakPostParametersCallbackMethod | str, open_enum_validator(V2SpeakPostParametersCallbackMethod)
]
