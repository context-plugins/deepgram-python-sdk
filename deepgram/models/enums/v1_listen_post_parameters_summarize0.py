from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ListenPostParametersSummarize0(str, Enum):
    V2 = "v2"

    __str__ = str.__str__


V1ListenPostParametersSummarize0OrStr: TypeAlias = Annotated[
    V1ListenPostParametersSummarize0 | str, open_enum_validator(V1ListenPostParametersSummarize0)
]
