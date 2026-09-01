from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ListenPostParametersDiarizeModel(str, Enum):
    LATEST = "latest"
    V1 = "v1"
    V2 = "v2"

    __str__ = str.__str__


V1ListenPostParametersDiarizeModelOrStr: TypeAlias = Annotated[
    V1ListenPostParametersDiarizeModel | str, open_enum_validator(V1ListenPostParametersDiarizeModel)
]
