from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ReadPostParametersCallbackMethod(str, Enum):
    POST = "POST"
    PUT = "PUT"

    __str__ = str.__str__


V1ReadPostParametersCallbackMethodOrStr: TypeAlias = Annotated[
    V1ReadPostParametersCallbackMethod | str, open_enum_validator(V1ReadPostParametersCallbackMethod)
]
