from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ListenPostParametersCallbackMethod(str, Enum):
    POST = "POST"
    PUT = "PUT"

    __str__ = str.__str__


V1ListenPostParametersCallbackMethodOrStr: TypeAlias = Annotated[
    V1ListenPostParametersCallbackMethod | str, open_enum_validator(V1ListenPostParametersCallbackMethod)
]
