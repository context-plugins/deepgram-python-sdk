from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1SpeakPostParametersCallbackMethod(str, Enum):
    POST = "POST"
    PUT = "PUT"

    __str__ = str.__str__


V1SpeakPostParametersCallbackMethodOrStr: TypeAlias = Annotated[
    V1SpeakPostParametersCallbackMethod | str, open_enum_validator(V1SpeakPostParametersCallbackMethod)
]
